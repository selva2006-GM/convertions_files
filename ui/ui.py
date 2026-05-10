import tkinter as tk
from collections import deque
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk
import os
import win32gui
import win32ui
import win32con
import win32api
from win32com.shell import shell, shellcon

stack = deque()
class Gui:
    
    
    
    def __init__(self, root):
        self.root = root
        
        self.root.title("Media Manager")
        self.root.geometry("700x500")
        self.root.config(bg = "#1e1e2f")
        self.root.resizable(False, False)
        self.stack = deque()
        
        
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
            ("Select Document", self.select_document)
        ]

        self.mainscreen(texttitle, buttons)
    def image(self):
        
        texttitle = "Image Section"

        buttons = [
            ("Select Image", self.select_document)
        ]

        self.mainscreen(texttitle, buttons)
    def video(self):
        texttitle = "video Section"

        buttons = [
            ("Select Video", self.select_document)
        ]

        self.mainscreen(texttitle, buttons)
    def audio(self):
        texttitle = "Audio Section"

        buttons = [
            ("Select Document", self.select_document)
        ]

        self.mainscreen(texttitle, buttons)
    def select_document(self):
        
        
    #     self.clear_frame()

    #     self.title = tk.Label(
    #         self.root,
    #         text="Drop File",
    #         font=("Arial", 24, "bold"),
    #         bg="#1e1e2f",
    #         fg="white"
    #     )

    #     self.title.pack(pady=20)

    #     self.frame = tk.Frame(
    #         self.root,
    #         bg="#1e1e2f"
    #     )

    #     self.frame.pack(expand=True)

    #     self.drop_label = tk.Label(
    #         self.frame,
    #         text="Drop File Here",
    #         font=("Arial", 16),
    #         bg="lightgray",
    #         width=30,
    #         height=5
    #     )

    #     self.drop_label.pack(pady=20)

    #     self.icon_label = tk.Label(
    #         self.frame,
    #         bg="#1e1e2f"
    #     )

    #     self.icon_label.pack()

    #     self.drop_label.drop_target_register(DND_FILES)

    #     self.drop_label.dnd_bind(
    #         "<<Drop>>",
    #         self.drop_file
    #     )
    # def drop_file(self, event):

    #     file_path = event.data.strip("{}")

    #     print(file_path)

    #     photo = self.get_file_icon(file_path)

    #     if photo:

    #         self.icon_label.config(image=photo)

    #         self.icon_label.image = photo
    
    # def get_file_icon(self, file_path):

    #     flags = (
    #         shellcon.SHGFI_ICON |
    #         shellcon.SHGFI_LARGEICON
    #     )

    #     result = shell.SHGetFileInfo(
    #         file_path,
    #         0,
    #         flags
    #     )

    #     hicon = result[0]

    #     if hicon == 0:
    #         return None

    #     hdc = win32ui.CreateDCFromHandle(
    #         win32gui.GetDC(0)
    #     )

    #     hbmp = win32ui.CreateBitmap()

    #     hbmp.CreateCompatibleBitmap(hdc, 64, 64)

    #     hdc_mem = hdc.CreateCompatibleDC()

    #     hdc_mem.SelectObject(hbmp)

    #     win32gui.DrawIconEx(
    #         hdc_mem.GetHandleOutput(),
    #         0,
    #         0,
    #         hicon,
    #         64,
    #         64,
    #         0,
    #         None,
    #         win32con.DI_NORMAL
    #     )

    #     bmpinfo = hbmp.GetInfo()

    #     bmpstr = hbmp.GetBitmapBits(True)

    #     image = Image.frombuffer(
    #         'RGBA',
    #         (
    #             bmpinfo['bmWidth'],
    #             bmpinfo['bmHeight']
    #         ),
    #         bmpstr,
    #         'raw',
    #         'BGRA',
    #         0,
    #         1
    #     )

    #     win32gui.DestroyIcon(hicon)

    #     return ImageTk.PhotoImage(image)