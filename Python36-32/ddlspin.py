from tkinter import *
from tkinter import ttk

root=Tk()
days=StringVar()
combobox=ttk.Combobox(root,value=["sun","mon","tues","wed","thurs","fri","sat"],textvariable=days)
combobox.pack()

spin=Spinbox(root,from_="1990",to="9999")
spin.pack()

img=PhotoImage(file="C:\\Users\\Mahe\\Pictures\\Saved Pictures\\nature.jpg")
minimage=img.subsample(15,10)

def showmessage():
    print("Button is clicked")

button=ttk.Button(root,text="click",command=showmessage(),image=minimage)
button.pack()

root.mainloop()
