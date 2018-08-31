from tkinter import *
from tkinter import ttk
from dbconnect import DBconnect

dconnect =DBconnect()


master = Tk()
def save():
    for k in range (0,5):
        print("TEST:{}".format(m[k]))
        print("result:{}".format(e[k].get()))
        print("unit:{}".format(f[k].get()))
     
e=[1,2,3,4,5]
f=[1,2,2,2,2]
Label(master,text="test").grid(row=0,column=0)
Label(master,text="result").grid(row=0,column=2)
Label(master,text="unit").grid(row=0,column=4)
m=["soil moisture","temperature","pressure","humidity","air quality","pH test"]
for i in range(0,5):
    Label(master, text=m[i]).grid(row=i+1,column=0)
    e[i]=Entry(master)
    e[i].grid(row=i+1,column=2)
    f[i]=Entry(master)
    f[i].grid(row=i+1,column=4)
b=ttk.Button(master,text="Save")
b.grid(row=6,column=4)
b.config(command=save)
for k in range(0,5):
    DBconnect.Add(m[k],e[k].get(),f[k].get())





mainloop( )
