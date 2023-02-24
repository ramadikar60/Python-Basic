import tkinter as tk
from tkinter import ttk

class MainApplication(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Contoh Style pada GUI")

        # membuat style dengan warna latar belakang hijau dan warna font putih
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("TFrame", background="#00aa00")
        self.style.configure("TLabel", foreground="#ffffff", background="#00aa00")
        self.style.configure("TButton", foreground="#ffffff", background="#004400")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="Halaman Awal", font=("Helvetica", 18))
        label.pack(side="top", fill="x", pady=10)

        button1 = ttk.Button(self, text="Pindah ke Halaman Satu", command=lambda: controller.show_frame("PageOne"))
        button1.pack()

        button2 = ttk.Button(self, text="Pindah ke Halaman Dua", command=lambda: controller.show_frame("PageTwo"))
        button2.pack()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="Halaman Satu", font=("Helvetica", 18))
        label.pack(side="top", fill="x", pady=10)

        button = ttk.Button(self, text="Kembali ke Halaman Awal", command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="Halaman Dua", font=("Helvetica", 18))
        label.pack(side="top", fill="x", pady=10)

        button = ttk.Button(self, text="Kembali ke Halaman Awal", command=lambda: controller.show_frame("StartPage"))
        button.pack()

app = MainApplication()
app.mainloop()