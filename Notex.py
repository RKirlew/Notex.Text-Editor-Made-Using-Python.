from Tkinter import *
import tkFileDialog
import os

root=Tk()
root.title("Notex Text Editor v.1.0")
#root.iconbitmap("notex.ico")

menu=Menu()
root.config(menu=menu)
subMenu=Menu(menu)
def saveAs():
    global text
    t=textentry.get("1.0","end-1c")
    savelocation=tkFileDialog.asksaveasfilename()
    file1=open(savelocation,"w+")
    file1.write(t)
    file1.close()
def exitEditor():
    sys.exit()
def Courier():
    global text
    textentry.config(font="Courier")
def Arial():
    global text
    textentry.config(font="Arial")
def Helvetica():
    global text
    textentry.config(font="Helvetica")
def Times():
    global text
    textentry.config(font="Times")
def comic():
    global text
    textentry.config(font="Symbol")
def black():
    textentry.config(background="black" ,fg="white")
def green():
    textentry.config(background="green")
def yellow():
    textentry.config(background="yellow")
def redText():
    textentry.config(fg="red")
def yText():
    textentry.config(fg="yellow")    
def gText():
    textentry.config(fg="green")
def pText():
    textentry.config(fg="purple")
def bText():
    textentry.config(fg="blue")
def oText():
    textentry.config(fg="orange")
def brText():
    textentry.config(fg="brown")
def wText():
    textentry.config(fg="white")
def blackText():
    textentry.config(fg="black")
    
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="Save As",command=saveAs)

CloseEditor=Menu(menu)
menu.add_cascade(label="Program",menu=CloseEditor)
CloseEditor.add_command(label="Exit", command=exitEditor)
fEditor=Menu(menu)
menu.add_cascade(label="Customization",menu=fEditor)
fEditor.add_command(label="Courier",command=Courier)
fEditor.add_command(label="Arial",command=Arial)
fEditor.add_command(label="Helvetica",command=Helvetica)
fEditor.add_command(label="Times New Roman",command=Times)
fEditor.add_command(label="Symbol",command=comic)
fEditor.add_command(label="Black Background",command=black)
fEditor.add_command(label="Green Background",command=green)
fEditor.add_command(label="Yellow Background",command=yellow)

FontColor=Menu(menu)
menu.add_cascade(label="Font Color",menu=FontColor)
FontColor.add_command(label="Black", command=blackText)
FontColor.add_separator()
FontColor.add_command(label="Red", command=redText)
FontColor.add_separator()
FontColor.add_command(label="Yellow", command=yText)
FontColor.add_separator()

FontColor.add_command(label="Green", command=gText)
FontColor.add_separator()

FontColor.add_command(label="Purple", command=pText)
FontColor.add_separator()

FontColor.add_command(label="Blue", command=bText)
FontColor.add_separator()

FontColor.add_command(label="Orange", command=oText)
FontColor.add_separator()

FontColor.add_command(label="Brown", command=brText)
FontColor.add_separator()

FontColor.add_command(label="White", command=wText)




textentry=Text(root,width=300,height=300,background="white")
textentry.pack()




    
root.mainloop()


