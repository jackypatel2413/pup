from tkinter import * 
import tkinter as tk

top = Tk()
top.geometry("300x200")
 
l = Label(top,text = "Message boxes",font=50)
l.pack()

messagebox.showinfo("showinfo", "Information")
messagebox.showwarning("showwarning", "Warning")
messagebox.showerror("showerror", "Error")
messagebox.askquestion("askquestion", "Are you sure?")
messagebox.askokcancel("askokcancel", "Want to continue?")
messagebox.askyesno("askyesno", "Find the value?") 
messagebox.askretrycancel("askretrycancel", "Try again?") 

top.mainloop()
