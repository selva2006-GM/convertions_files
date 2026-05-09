import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class MediaUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Media Manager")
        self.root.geometry("500x350")
        self.root.config(bg="#1e1e2f")
        self.menu()
    def menu(self):
        self.title = tk.Label(
            root,
            text="Choose a Category",
            font=("Arial", 22, "bold"),
            bg="#1e1e2f",
            fg="white"
        )
        self.title.pack(pady=25)

        self.button_frame = tk.Frame(root, bg="#1e1e2f")
        self.button_frame.pack(pady=20)

        rootbuttons = [
            ("Documents", self.documents),
            ("Image", self.image),
            ("Video", self.video),
            ("Audio", self.audio)
        ]

        row = 0
        col = 0

        for text, command in rootbuttons:
            btn = tk.Button(
                self.button_frame,
                text=text,
                command=command,
                width=25,
                height=3,
                font=("Arial", 12, "bold"),
                bg="#4a90e2",
                fg="white",
                activebackground="#357abd",
                cursor="hand2"
            )

            btn.grid(row=row, column=col, padx=15, pady=15)
            row += 1

    def documents(self):
        self.remove()
        self.title.config(
            text = "Select Document",
            font = ("Arial", 20, "bold"),
            fg = "white",
            bg="black"
        )
        btn = tk.Button(
                self.button_frame,
                text="Select the file",
                command=self.select_file,
                width=25,
                height=3,
                font=("Arial", 12, "bold"),
                bg="#4a90e2",
                fg="white",
                activebackground="#357abd",
                cursor="hand2"
            )

        btn.grid(row=4, column=4, padx=15, pady=15)
        
    def select_file(self):
        file_path = filedialog.askopenfilename()
        print("file path : ", file_path)
        print("file type: ", file_path.split(".")[1])
        
    def remove(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()

    def image(self):
        messagebox.showinfo("Image", "Image Button Clicked")

    def video(self):
        messagebox.showinfo("Video", "Video Button Clicked")

    def audio(self):
        messagebox.showinfo("Audio", "Audio Button Clicked")


root = tk.Tk()
app = MediaUI(root)
root.mainloop()