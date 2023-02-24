from tkinter import Tk, Frame, Menu
class membuatSubMenu(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.window = parent
        self.initUI()
        self.membuatMenu()
    def initUI(self):
        self.window.title("Python GUI")
        self.window.geometry("450x250")
    def membuatMenu(self):
        menubar = Menu(self.window)
        self.window.config(menu=menubar)
        fileMenu = Menu(menubar)
        submenu = Menu(fileMenu)
        submenu.add_command(label="New Feed")
        submenu.add_command(label="Bookmarks")
        submenu.add_command(label="Mail")
        fileMenu.add_cascade(label='Import', menu=submenu, underline=0)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", underline=0, command=self.onExit)
        menubar.add_cascade(label="File", underline=0, menu=fileMenu)
    def onExit(self):
        self.quit()
if __name__ == '__main__':
    root = Tk()
    app = membuatSubMenu(root)
    root.mainloop()