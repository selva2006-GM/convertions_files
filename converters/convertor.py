from tkinter.filedialog import asksaveasfilename
import subprocess
import os
from tree.tree import find_path


class FileConverter:

    def __init__(self, input_file, selected, category):
        print("input_file :", input_file)
        print("selected : ", selected)
        print("category : ", category)
        self.input_file = input_file
        self.output_format = selected
        self.category = category
        self.category = category
        
        self.current_file_type = self.input_file.split(".")[-1]
        self.output_file_type =  selected
        
