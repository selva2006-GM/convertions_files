from reportlab.pdfgen import canvas 
import fitz


CONVERTERS = {
    ("txt", "pdf"): txt_to_pdf,
    ("pdf", "txt"): pdf_to_txt,
    ("txt", "html"): txt_to_html,
}


