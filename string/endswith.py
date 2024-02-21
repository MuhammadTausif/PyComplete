filename = "report.pdf"
if filename.endswith(".pdf"):
    print("Ready for distribution!")

#  Example 2: URL Validation

url = "https://example.com/welcome.html"
if url.endswith(".html"):
    print("This is an HTML page.")

# Example 3: String Pattern Checking

quote = "All's well that ends well."
if quote.endswith("well."):
    print("The quote ends with 'well.'")


# Example 4: Multiple Options Check

file_name = "presentation.pptx"
if file_name.endswith((".pptx", ".ppt", ".pdf")):
    print("The file is ready for the meeting.")