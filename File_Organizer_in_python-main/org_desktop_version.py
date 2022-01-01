import os 
import shutil
from tkinter import *

root  = Tk()
root.configure(bg="#934434")
root.title("File Organizer")

def org(path):
    files = os.listdir(path)
    for file in files:
        filename,extenstion = os.path.splitext(file)
        extenstion = extenstion[1:]
        if os.path.exists(path + "/" + extenstion):
            shutil.move(path + "/" + file, path + "/" + extenstion + "/" + file)
        else:
            os.makedirs(path +"/"+ extenstion)
            shutil.move(path + "/" + file, path + "/" + extenstion)
    #return "done!"
    

e = Entry(root,width=80,borderwidth=3)
e.pack()

def buttonfunc():
    org(e.get())

myButton = Button(root, text="Run",bg="#99D9DF",fg="#232323",command=buttonfunc,padx=30,pady=3)
myButton.pack()

root.mainloop()
