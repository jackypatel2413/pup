import tkinter as tk

window = tk.Tk()
window.title("Exam_Task")
window.geometry("800x500")

var = tk.StringVar()
# l = tk.Label(window, bg='lightblue', width=200, height=100, text='')
# l.pack()

# var = tk.StringVar()
# l1 = tk.Label(window, bg='white', width=50, height=50, text='')
# l1.place(x=1, y=0)
# l1.pack()

lb1 = tk.Label(window, text="First Name:", width=12, font=("arial", 12))
lb1.place(x=20, y=40)
en1 = tk.Entry(window)
en1.place(x=180, y=40)

lb3 = tk.Label(window, text="Last Name:", width=12, font=("arial", 12))
lb3.place(x=20, y=70)
en3 = tk.Entry(window)
en3.place(x=180, y=70)

# lb4 = tk.Label(window, text="Contact Number", width=13, font=("arial", 12))
# lb4.place(x=20, y=100)
# en4 = tk.Entry(window)
# en4.place(x=200, y=100)

lb5 = tk.Label(window, text="Select Gender:", width=12, font=("arial", 12))
lb5.place(x=20, y=100)
vars = tk.IntVar()
tk.Radiobutton(window, text="Male", padx=5, variable=vars,
               value=1).place(x=180, y=100)
tk.Radiobutton(window, text="Female", padx=10,
               variable=vars, value=2).place(x=240, y=100)
tk.Radiobutton(window, text="others", padx=15,
               variable=vars, value=3).place(x=310, y=100)

lb6 = tk.Label(window, text="Languages:", width=12, font=("arial", 12))
lb6.place(x=20, y=130)
Checkbutton1 = tk.IntVar()

Checkbutton2 = tk.IntVar()

Checkbutton3 = tk.IntVar()
tk.Checkbutton(window, text="Telugu", padx=5, variable=Checkbutton1,
               onvalue=1, offvalue=0).place(x=180, y=130)
tk.Checkbutton(window, text="English", padx=10,
               variable=Checkbutton2, onvalue=1, offvalue=0).place(x=240, y=130)
tk.Checkbutton(window, text="Hindi", padx=15,
               variable=Checkbutton3, onvalue=1, offvalue=0).place(x=310, y=130)

lb7 = tk.Label(window, text="Email:", width=12, font=("arial", 12))
lb7.place(x=20, y=160)
en4 = tk.Entry(window)
en4.place(x=180, y=160)

lb7 = tk.Label(window, text="Address:", width=12, font=("arial", 12))
lb7.place(x=20, y=190)
en4 = tk.Text(window, width=30, height=5)
en4.place(x=180, y=190)

list_of_state = ("Gujrat", "Maharastra", "Delhi", "Chennai")
cv = tk.StringVar()
drplist = tk.OptionMenu(window, cv, *list_of_state)
drplist.config(width=15)
cv.set("Choose State")
lb2 = tk.Label(window, text="State", width=12, font=("arial", 12))
lb2.place(x=20, y=280)
drplist.place(x=180, y=280)

lb6 = tk.Label(window, text="Zip", width=12, font=("arial", 12))
lb6.place(x=20, y=320)
en6 = tk.Entry(window)
en6.place(x=180, y=320)

list_of_type = ("Rewards credit cards", "Secured credit cards",
                "Interest credit cards", "Cashback credit cards")
cv = tk.StringVar()
drplist = tk.OptionMenu(window, cv, *list_of_type)
drplist.config(width=20)
cv.set("Choose Credit Card Type")
lb2 = tk.Label(window, text="Credit Card Type", width=15, font=("arial", 12))
lb2.place(x=20, y=350)
drplist.place(x=180, y=350)


window.mainloop()