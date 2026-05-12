from tkinter.filedialog import asksaveasfilename
import subprocess
import os


class FileConverter:

    def __init__(self, input_file, selected, category):

        self.input_file = input_file
        self.output_format = selected
        self.category = category

        if self.category == "doc":
            self.document_converter()

    def document_converter(self):

        output_file = asksaveasfilename(
            defaultextension=f".{self.output_format}",
            filetypes=[
                (f"{self.output_format.upper()} files",
                 f"*.{self.output_format}")
            ]
        )

        if not output_file:
            print("Cancelled")
            return

        output_dir = os.path.dirname(output_file)

        subprocess.run([
            r"C:\Program Files\LibreOffice\program\soffice.exe",
            "--headless",
            "--convert-to",
            self.output_format,
            self.input_file,
            "--outdir",
            output_dir
        ])

        # LibreOffice creates file automatically
        old_output = os.path.join(
            output_dir,
            os.path.splitext(
                os.path.basename(self.input_file)
            )[0] + f".{self.output_format}"
        )

        os.rename(old_output, output_file)

        print("Conversion completed")