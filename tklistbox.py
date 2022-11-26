from tkinter import * 
import tkinter as tk

top = Tk()
lb = Listbox(top,height=5,width=15,bg="grey",activestyle="dotbox",font="Helvetica",fg="yellow")
 
top.geometry("300x200")
l = Label(top,text = "Food Items")

lb.insert(1,"Nachos")
lb.insert(2,"Pizza")
lb.insert(3,"Maggi")
lb.insert(4,"Dosa")

l.pack()
lb.pack()
top.mainloop()
