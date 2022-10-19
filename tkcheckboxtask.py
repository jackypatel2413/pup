import tkinter as tk

window = tk.Tk()
window.title("Window")
window.geometry("600x500")

a = tk.Checkbutton(text='Chocholate Ice-Cream')
a.place(x=10,y=20)

b = tk.Checkbutton(window ,text='Mango Ice-Cream')
b.place(x=10,y=50)

c = tk.Checkbutton(window ,text='Dark Chocholate Ice-Cream')
c.place(x=10,y=80)

d = tk.Checkbutton(window ,text='Butterscotch Ice-Cream')
d.place(x=10,y=110)

e = tk.Checkbutton(window ,text='oreo ice-cream')
e.place(x=10,y=110)



window.mainloop()