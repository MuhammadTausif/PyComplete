import docx
import pdfkit

pdfkit.from_url('http://google.com', 'out.pdf')
pdfkit.from_file('test.html', 'out.pdf')
pdfkit.from_string('Hello!', 'out.pdf')

# class DocumentGenerator:
#     def generate_document(self, content):
#         pass

# class DocxGenerator(DocumentGenerator):
#     def generate_document(self, content):
#         document = docx.Document()
#         document.add_paragraph(content)
#         document.save("document.docx")
#         print("Docx document generated.")

# class PdfGenerator(DocumentGenerator):
#     def generate_document(self, content):
#         pdfkit.from_string(content, "document.pdf")
#         print("PDF document generated.")

# # Usage
# generator = DocxGenerator()
# generator.generate_document("This is a document in DOCX format.")

# generator = PdfGenerator()
# generator.generate_document("This is a document in PDF format.")