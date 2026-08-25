from PyPDF2 import PdfReader

# Load PDF
reader = PdfReader("pdf-test.pdf")

# Store all extracted text
full_text = ""

# Read every page
for page in reader.pages:
    text = page.extract_text()
    
    if text:
        full_text += text + "\n"

# Print text
print(full_text)

# Save into a text file
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(full_text)

print("PDF converted to text successfully!")