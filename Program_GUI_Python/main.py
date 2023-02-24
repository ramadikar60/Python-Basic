from tkinter import Tk, Frame, Menu

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.window = parent
        self.initUI()
        self.membuatMenu()
    def initUI(self):
        self.window.title("Membuat Menu Bar")
        self.window.geometry("250x150")
    def membuatMenu(self):
        menubar = Menu(self.window)
        self.window.config(menu = menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.perintahKeluar)
        menubar.add_cascade(label="File", menu=fileMenu)
    def perintahKeluar(self):
        self.quit()
if __name__ == '__main__':
    root = Tk()
    app = Example(root)
    root.mainloop()