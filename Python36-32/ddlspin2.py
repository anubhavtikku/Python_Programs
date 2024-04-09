from tkinter import *
from tkinter import ttk

root=Tk()
def printno(n):
    print(n)

button1=ttk.Button(root,text="click",command=lambda:printno(7))
button1.pack()

button2=ttk.Button(root,text="click",command=lambda:printno(7))
button2.pack()

root.mainloop()
