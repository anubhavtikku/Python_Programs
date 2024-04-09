from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import MySQLdb as db

conn=db.connect("127.0.0.1","root","tiger","hr")
cur=conn.cursor()

def showrecord(j):
    selqry="select * from dummy where employee_id="+j
    cur.execute(selqry)
    rs=cur.fetchall()
    text.config(state='normal')
    text.delete('1.0','3.0 lineend')
    text.insert('1.0',rs)
    messagebox.showinfo(title="Record Details ",message=rs)
    text.config(state='disabled')

root=Tk()

label=Label(root,text="Select record")
label.config(wraplength=320)
label.pack()

spin=Spinbox(root,from_="100",to="206")
spin.pack()

button=ttk.Button(root,text="Show record",command=lambda:showrecord(spin.get()))
button.pack()


text=Text(root,width=40,height=10)
text.pack()
text.config(state='disabled')


label2=Label(root,text="\n\nUpdate Record")
label2.config(wraplength=320)
label2.pack()

