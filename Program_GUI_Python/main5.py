from tkinter import *
master = Tk()
menubar = Menu(master)
def Save():
    print('Save')
def Help():
    print('Help')
def About():
    print('About')
def Quit():
    print('Quit')

menubar.add_command(label='Save', command=Save)
menubar.add_command(label='Help', command=Help)
menubar.add_command(label='About', command=About)
menubar.add_command(label='Quit', command=master.quit)
master.config(menu=menubar)
mainloop()