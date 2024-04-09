from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup
import urllib.request
from PIL import ImageTk, Image
import io
import re;

root=Tk()
frame=ttk.Frame(root,width=600,height=400)
frame.pack()

imagelist=[]
url="https://www.imdb.com/chart/top";
response=urllib.request.urlopen(url);
readhtml=response.read()
bs=BeautifulSoup(readhtml)
response.close()
ro=1
co=1

for col in bs.find_all("td", {"class": ["posterColumn"]}):
    path=col.find_next("img")["src"]
    print(path)
    rawdata=urllib.request.urlopen(path).read()
    im=Image.open(io.BytesIO(rawdata))
    photo=ImageTk.PhotoImage(im);
    imagelist.append(photo)
    if(co%25==0):
        ttk.Label(frame,image=photo,relief=GROOVE,background='blue').grid(row=ro,column=co)
        co=1
        ro=ro+1
    else:
        ttk.Label(frame, image=photo,relief=GROOVE,background='blue').grid(row=ro,column=co)
        co = co + 1





root.mainloop()
