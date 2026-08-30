import tkinter as tk
from collections import deque
from tkinter import ttk
from PIL import Image, ImageTk
import os
from tkinter.filedialog import askopenfilename
from converters.convertor import FileConverter
stack = deque()
class Gui:

    def __init__(self, root):
        self.root = root
        
        self.root.title("Media Manager")
        self.root.geometry("700x500")
        self.root.config(bg = "#1e1e2f")
        self.root.resizable(False, False)
        self.stack = deque()
        
        self.formats = {
    "doc": [
        "pdf", "txt", "docx", "doc", "rtf", "odt",
        "xls", "xlsx", "csv",
        "ppt", "pptx",
        "html", "xml", "json"
    ],

    "img": [
        "png", "jpg", "jpeg", "gif", "bmp",
        "webp", "tiff", "ico", "svg"
    ],

    "vid": [
        "mp4", "mkv", "avi", "mov", "wmv",
        "flv", "webm", "mpeg", "mpg", "3gp"
    ],

    "aud": [
        "mp3", "wav", "aac", "flac", "ogg",
        "m4a", "wma", "aiff", "opus"
    ],

    "code": [
        "py", "java", "cpp", "c", "js",
        "ts", "html", "css", "php",
        "rb", "go", "rs", "swift", "kt"
    ],

    "archive": [
        "zip", "rar", "7z", "tar",
        "gz", "bz2", "xz"
    ]
}
        self.mainscreen()
        
    def mainscreen(
        self,
        texttitle = "Choose a Category",
        buttons = None,
        save = True
        ):
        
        if save:
            self.stack.append(
                (texttitle, buttons)
            )
        self.clear_frame()
        
        if buttons is None:
            buttons = [
            ("Documents", self.documents),
            ("Image", self.image),
            ("Video", self.video),
            ("Audio", self.audio)
         ]
        
        
        self.title = tk.Label(
            self.root,
            text=texttitle,
            font=("Arial", 24, "bold"),
            bg="#1e1e2f",
            fg="white"
        )
        
        self.title.pack( pady=20)
        self.frame = tk.Frame( self.root, bg="#1e1e2f")
        self.frame.pack(expand=True)
        
        if len(self.stack) > 1:
            back_btn = tk.Button(
                self.root,
                text="← Back",
                command = self.go_back,
                bg = "#ff5555",
                fg = "white",
                font = ("Arail", 10, "bold")
            )
            back_btn.place(x=20, y=20)
            
        
        for i, (text, command) in enumerate(buttons):

            btn = self.create_button(text, command)

            btn.grid(
                row=i,
                column=0,
                padx=20,
                pady=15
            )
        
    def go_back(self):
        self.stack.pop()
        
        texttitle, buttons = self.stack[-1]
        
        self.mainscreen(
            texttitle,
            buttons,
            save = False
            )        
        
    def create_button(self, text, command):
        
        button = tk.Button(
            self.frame,
            text = text,
            command = command,
            width=25,
            height=2,
            font=("Arial", 12, "bold"),
            bg="#4a90e2",
            fg="white",
            activebackground = "#357abd",
            activeforeground = "white",
            cursor="hand2",
            relief="flat"
        )
        return button
        
    def clear_frame(self):
        if hasattr(self, "frame"):
            self.frame.destroy()

        if hasattr(self, "title"):
            self.title.destroy()
        
    
    def documents(self):
        texttitle = "Document Section"

        buttons = [
            ("Select Document", lambda : self.select_document("doc"))
        ]

        self.mainscreen(texttitle, buttons)
    def image(self):
        
        texttitle = "Image Section"

        buttons = [
            ("Select Image", lambda : self.select_document("img"))
        ]

        self.mainscreen(texttitle, buttons)
    def video(self):
        texttitle = "video Section"

        buttons = [
            ("Select Video",lambda : self.select_document("vid"))
        ]

        self.mainscreen(texttitle, buttons)
    def audio(self):
        texttitle = "Audio Section"

        buttons = [
            ("Select Document", lambda :  self.select_document("aud"))
        ]

        self.mainscreen(texttitle, buttons)
    def select_document(self,category  = "doc"):
        
        extension = " ".join(f"*.{ext}" for ext in self.formats[category])
        file_path = askopenfilename(
            filetypes=[
                (f"{category} files ", extension)
            ]
        )
        
        extension = os.path.splitext(file_path)[1]
        
        self.select_btn = self.create_button("select the format",lambda : self.select_format(file_path, extension, category ))
        self.select_btn.grid(
                row=10,
                column=0,
                padx=20,
                pady=15
            )
        
    def select_format(self, file_path, extension, category):
        options = [
            file_type
            for file_cat in self.formats
            for file_type in self.formats[file_cat]
        ]
        selected = tk.StringVar()
        
        self.dropdown = ttk.Combobox(
            self.frame,
            textvariable=selected,
            values=options,
            state="normal"
        )
        
        self.dropdown.grid(
            row = 10,
            column = 0,
            padx = 20,
            pady = 15
        )
        
        def search(event):
            typed = selected.get().lower()
            
            filtered = [
                file_type
                for file_type in options
                if typed in file_type.lower()
            ]
            
            self.dropdown["values"] = filtered
            
            if filtered:
                self.dropdown.event_generate("<Down>")
        self.dropdown.bind("<KeyRelease>", search)
        
        btn = self.create_button("Start convertion",
            lambda: self.convertion(
                file_path,
                extension,
                selected.get(),
                category
                )
            )
        btn.grid(
            row = 14,
            column = 0,
            padx = 20,
            pady = 15
        )
    def convertion(self,file_path, extension, selected, category):
        print(file_path, selected, category)
        FileConverter(file_path, selected, category)