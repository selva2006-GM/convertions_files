import csv
import json
from reportlab.pdfgen import canvas


class FileConverter:

    def txt_to_pdf(self, input_file, output_file):

        with open(input_file, "r") as file:
            lines = file.readlines()

        pdf = canvas.Canvas(output_file)

        y = 800

        for line in lines:
            pdf.drawString(50, y, line.strip())
            y -= 20

        pdf.save()

        print("TXT converted to PDF successfully!")



    def csv_to_json(self, input_file, output_file):

        data = []

        with open(input_file, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:
                data.append(row)

        with open(output_file, "w") as file:
            json.dump(data, file, indent=4)

        print("CSV converted to JSON successfully!")



    def txt_to_md(self, input_file, output_file):

        with open(input_file, "r") as file:
            content = file.read()

        with open(output_file, "w") as file:
            file.write("# Converted Markdown File\n\n")
            file.write(content)

        print("TXT converted to MD successfully!")



class UserInterface:

    def __init__(self):

        self.converter = FileConverter()



    def menu(self):

        print("\n===== FILE CONVERTER =====")
        print("1. TXT -> PDF")
        print("2. CSV -> JSON")
        print("3. TXT -> MD")

        choice = int(input("Enter your choice: "))

        input_file = input("Enter input file name: ")
        output_file = input("Enter output file name: ")

        if choice == 1:
            self.converter.txt_to_pdf(input_file, output_file)

        elif choice == 2:
            self.converter.csv_to_json(input_file, output_file)

        elif choice == 3:
            self.converter.txt_to_md(input_file, output_file)

        else:
            print("Invalid choice!")



obj = UserInterface()
obj.menu()