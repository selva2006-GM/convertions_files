from reportlab.pdfgen import canvas
import fitz
import librosa
import librosa.display
import matplotlib.pyplot as plt

from PIL import Image
from PIL.PngImagePlugin import PngInfo


def audio_to_image(audio_path, image_path):
    with open(audio_path, "rb") as f:
        audio_data = f.read()

    # Create a 1x1 transparent PNG
    image = Image.new("RGBA", (1, 1), (0, 0, 0, 0))

    metadata = PngInfo()
    metadata.add_text("audio_data", audio_data.hex())
    metadata.add_text("audio_filename", audio_path)

    image.save(image_path, "PNG", pnginfo=metadata)

    return image_path


def image_to_audio(image_path, audio_path):
    image = Image.open(image_path)

    metadata = image.info

    if "audio_data" not in metadata:
        raise ValueError(
            "This PNG does not contain embedded audio data."
        )

    audio_data = bytes.fromhex(metadata["audio_data"])

    with open(audio_path, "wb") as f:
        f.write(audio_data)

    return audio_path

def audio_to_spectrogram(audio_path, output_path="spectrogram.png"):
    audio, sample_rate = librosa.load(
        audio_path,
        sr=None,
        mono=True
    )

    spectrogram = librosa.feature.melspectrogram(
        y=audio,
        sr=sample_rate
    )

    spectrogram_db = librosa.power_to_db(
        spectrogram,
        ref=max
    )

    plt.figure(figsize=(12, 5))

    librosa.display.specshow(
        spectrogram_db,
        sr=sample_rate,
        x_axis="time",
        y_axis="mel"
    )

    plt.colorbar(format="%+2.0f dB")
    plt.title("Audio Spectrogram")
    plt.tight_layout()

    plt.savefig(output_path, dpi=150)
    plt.close()

    return output_path

def pdf_to_html(current_file, next_file):
    print(current_file, "->", next_file)

    pdf = fitz.open(current_file)

    html_parts = []

    for page in pdf:
        html_parts.append(page.get_text("html"))

    with open(next_file, "w", encoding="utf-8") as file:
        file.write(
            "\n".join(html_parts)
        )

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



def jpg_to_pdf(current_file, next_file):
    print(current_file, "->", next_file)

    image = fitz.open(current_file)

    pdf = fitz.open()

    page = pdf.new_page(
        width=image[0].rect.width,
        height=image[0].rect.height
    )

    page.insert_image(
        page.rect,
        filename=current_file
    )

    pdf.save(next_file)

    image.close()
    pdf.close()

CONVERTERS = {
    ("mp3", "png"): audio_to_image,
    ("wav", "png"): audio_to_image,
    ("m4a", "png"): audio_to_image,
    ("flac", "png"): audio_to_image,
    ("ogg", "png"): audio_to_image,

    ("mp3", "jpg"): audio_to_image,
    ("wav", "jpg"): audio_to_image,
    ("m4a", "jpg"): audio_to_image,
    ("flac", "jpg"): audio_to_image,
    ("ogg", "jpg"): audio_to_image,
}