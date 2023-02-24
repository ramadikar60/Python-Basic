from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('Text Editor')
# root.iconbitmap('c:/gui/test.ico')
root.geometry("600x400")

# Buat main frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Buat scrollbar untuk text box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Buat text box
my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

# Configurasi scrollbar
text_scroll.config(command=my_text.yview)

# Buat menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Tambah menu file
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

# Tambah menu edit
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

# Tambah status bar untuk di bawah app
status_bar = Label(root, text='Ready     ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

root.mainloop()