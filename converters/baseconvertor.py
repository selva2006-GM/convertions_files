from reportlab.pdfgen import canvas
import fitz
from weasyprint import HTML


def pdf_to_html(current_file, next_file):
    print(current_file, "->", next_file)

    pdf = fitz.open(current_file)

    html_parts = []

    for page in pdf:
        html_parts.append(page.get_text("html"))

    with open(next_file, "w", encoding="utf-8") as file:
        file.write("\n".join(html_parts))

    pdf.close()


def txt_to_pdf(current_file, next_file):
    print(current_file, "->", next_file)

    with open(current_file, "r", encoding="utf-8") as file:
        text = file.read()

    pdf = canvas.Canvas(next_file)

    y = 800

    for line in text.splitlines():
        pdf.drawString(50, y, line)
        y -= 20

        if y < 50:
            pdf.showPage()
            y = 800

    pdf.save()


def pdf_to_txt(current_file, next_file):
    print(current_file, "->", next_file)

    pdf = fitz.open(current_file)

    with open(next_file, "w", encoding="utf-8") as file:
        for page in pdf:
            file.write(page.get_text())
            file.write("\n")

    pdf.close()


def txt_to_html(current_file, next_file):
    print(current_file, "->", next_file)

    with open(current_file, "r", encoding="utf-8") as file:
        text = file.read()

    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Converted File</title>
</head>
<body>
<pre>{text}</pre>
</body>
</html>
"""

    with open(next_file, "w", encoding="utf-8") as file:
        file.write(html)


def html_to_pdf(current_file, next_file):
    print(current_file, "->", next_file)

    HTML(filename=current_file).write_pdf(next_file)


CONVERTERS = {
    ("txt", "pdf"): txt_to_pdf,
    ("pdf", "txt"): pdf_to_txt,

    ("txt", "html"): txt_to_html,
    ("pdf", "html"): pdf_to_html,

    ("html", "pdf"): html_to_pdf,
}