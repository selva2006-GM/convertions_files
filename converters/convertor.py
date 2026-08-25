from tkinter.filedialog import asksaveasfilename
import subprocess
import os


class FileConverter:

    def __init__(self, input_file, selected, category):

        self.input_file = input_file
        self.output_format = selected
        self.category = category
        
        print("input file : ", self.input_file.split(",")[-1])
        print("output file : ", self.output_format)
        print("category : ", self.category)
        

        if self.category == "doc":
            self.document_converter()

    def document_converter(self):
        pass