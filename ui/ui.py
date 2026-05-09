import tkinter as tk
import Menu as menu
import Documentsc as doc
import Videoc as vi

class Gui:
    
    def __init__(self, root):
        self.root = root
        
        self.root.title("Media Manager")
        self.root.geometry("700x500")
        self.root.config(bg = "#1e1e2f")
        self.root.resizable(False, False)
        
    def mainscreen(self,
        texttitle = "Choose a Category",
         buttons = [
            ("Documents", doc.documents),
            ("Image", self.image),
            ("Video", self.video),
            ("Audio", self.audio)
        ]
                   ):
        
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
        
        for i, (text, command) in enumerate(buttons):

            btn = self.create_button(text, command)

            btn.grid(
                row=i,
                column=0,
                padx=20,
                pady=15
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
        for widget in self.frame.winfo_children():
            widget.destroy()
            