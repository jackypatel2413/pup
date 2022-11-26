import tkinter
import tkinter.ttk
root=tkinter.Tk()
root.geometry("700x500")

photo=PhotoImage(file = "a.png")
pi=photo.subsample(3,3)
Btn=tkinter.Button(root , text="click me" , image = pi )
Btn.grid(row=0,column=0)

root.mainloop()