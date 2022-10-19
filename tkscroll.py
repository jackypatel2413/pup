from tkinter import *

main=Tk()
main.geometry("400x300")
scroll=Scrollbar (main)
scroll.pack(fill=Y,side=RIGHT)
#listbox
lb=Listbox(main,height=8,yscrollcommand=scroll.set)
for i in range(31):
    lb.insert (END, "Number "+str(i))
lb.pack()

scroll.config(command=lb.yview)
main.mainloop()