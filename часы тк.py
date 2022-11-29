
from tkinter import *
import time

def timing():
    current = time.strftime("%H : %M : %S")
    clock.config(text=current)
    clock.after(200,timing)

root=Tk()

root.geometry("600x300")

clock=Label(root,font=("times",60,"bold"),bg="red")
clock.grid(row=2,column=2,pady=25,padx=100)
timing()

digital=Label(root,text="Часы на Питоне",font="times 24 bold")
digital.grid(row=0,column=2)

nota=Label(root,text="часов         минут        секунд",font="times 15 bold")
nota.grid(row=3,column=2)

root.mainloop()