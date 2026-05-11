import tkinter as tk
from collections import deque
from tkinterdnd2 import DND_FILES, TkinterDnD
from tkinter import ttk
from PIL import Image, ImageTk
import os
from tkinter.filedialog import askopenfilename

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
    "doc": ["pdf", "txt", "docx"],
    "img": ["png", "jpg", "jpeg", "gif"],
    "vid": ["mp4", "mkv", "avi"],
    "aud": ["mp3", "wav", "aac"]
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
    def select_document(self, filetype = "doc"):
        
        file_path = askopenfilename()
        
        extension = os.path.splitext(file_path)[1]
        
        self.select_btn = self.create_button("select the format",lambda : self.select_format(file_path, extension, filetype))
        self.select_btn.grid(
                row=10,
                column=0,
                padx=20,
                pady=15
            )
        
    def select_format(self, file_path, extension, filetype):
        options = self.formats[filetype]

        self.selected = tk.StringVar()

        self.dropdown = ttk.Combobox(
            self.frame,
            textvariable=self.selected,
            values=options,
            state="readonly"
        )

        self.dropdown.grid(
                row=10,
                column=0,
                padx=20,
                pady=15
            )
        
        btn = self.create_button("start convertion",lambda :  self.convertion(file_path, extension, self.selected))
        btn.grid(
                row=14,
                column=0,
                padx=20,
                pady=15
            )
        
    def convertion(self,file_path, extension, selected):
        print("starting convertion")