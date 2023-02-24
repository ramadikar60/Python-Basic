import tkinter as tk

class Halaman1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Hello World", font=("Helvetica", 18))
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Pindah ke Halaman 2", command=lambda: controller.show_frame(Halaman2))
        button.pack()

class Halaman2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Halo Dunia", font=("Helvetica", 18))
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Pindah ke Halaman 1", command=lambda: controller.show_frame(Halaman1))
        button.pack()

class Aplikasi(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        # membuat window utama
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # membuat halaman-halaman
        self.frames = {}
        for halaman in (Halaman1, Halaman2):
            frame = halaman(container, self)
            self.frames[halaman] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Halaman1)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

app = Aplikasi()
app.mainloop()