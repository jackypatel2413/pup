import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
name_var = tk.StringVar()
passw_var = tk.StringVar()
details_var = tk.StringVar()
def submit():

    name = name_var.get()
    password = passw_var.get()
    label_name = tk.Label(text="The name is: "+name)
    label_password = tk.Label(text="The password is: "+password)
    label_name.place(x=2, y=100)
    label_password.place(x=2, y=120)
    name_var.set("")
    passw_var.set("")


name_label = tk.Label(root, text='Username',
                      font=('Arial', 10, 'bold'))

name_entry = tk.Entry(root, textvariable=name_var,
                      font=('Arial', 10, 'normal'))

passw_label = tk.Label(root, text='Password', font=('Arial', 10, 'bold'))

passw_entry = tk.Entry(root, textvariable=passw_var,
                       font=('Arial', 10, 'normal'), show='*')

sub_btn = tk.Button(root, text='Submit', command=submit)

details_var = tk.Label(root, text="Details:-", font=('Arial', 15, 'bold'))

name_label.grid(row=0, column=0)

name_entry.grid(row=0, column=1)

passw_label.grid(row=1, column=0)

passw_entry.grid(row=1, column=1)

sub_btn.grid(row=2, column=1)

details_var.grid(row=4, column=0)

root.mainloop()