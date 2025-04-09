import os
import json
import PyPDF2
import re
import nltk
from collections import defaultdict
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize components
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + " "
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

def extract_text_from_txt(txt_path):
    """Extract text from a TXT file."""
    try:
        with open(txt_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"Error reading {txt_path}: {e}")
        return ""

def clean_text(text):
    """Tokenize, remove stopwords, numbers, and non-alphabetic words, and lemmatize."""
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\b\d+\b', '', text)  # Remove standalone numbers
    text = re.sub(r'\S*@\S*\s?', '', text)  # Remove email addresses
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'[^a-z\s]', '', text)  # Remove special characters and punctuation
    
    words = word_tokenize(text)
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words and len(word) > 2]
    
    return words

def build_inverted_index(folder_path):
    """Build an inverted index from files in the folder."""
    inverted_index = defaultdict(set)
    doc_id = 1
    doc_map = {}  # Mapping of doc_id to filenames

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Extract text based on file type
        if filename.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        elif filename.endswith(".txt"):
            text = extract_text_from_txt(file_path)
        else:
            continue  # Skip non-supported file types
        
        # Process the text and update inverted index
        words = clean_text(text)
        for word in words:
            inverted_index[word].add(doc_id)
        
        # Store document mapping
        doc_map[doc_id] = filename
        doc_id += 1
    
    # Convert sets to lists for JSON serialization
    inverted_index = {word: list(docs) for word, docs in inverted_index.items()}

    return inverted_index, doc_map

def save_index_to_json(inverted_index, doc_map, output_file="clean_inverted_index.json"):
    """Save the inverted index and document map to a JSON file."""
    index_data = {"inverted_index": inverted_index, "document_map": doc_map}
    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(index_data, json_file, indent=4)

if __name__ == "__main__":
    folder_path = input("Enter the folder path containing the documents: ").strip()
    inverted_index, doc_map = build_inverted_index(folder_path)
    save_index_to_json(inverted_index, doc_map)
    print(f"Cleaned inverted index saved as 'clean_inverted_index.json'")
