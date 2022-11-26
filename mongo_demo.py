from pymongo import MongoClient
from tkinter import*

root = Tk()
root.geometry("300x500")
client =MongoClient("localhost",27017)
col = database["student_info"]
database =client["student"]

# Insert

def HandleInsert():
    # db

    # collection
    
    name =e1.get()
    col.insert_one({'name':name})
    e1.delete(0,END)
    print("Data sucessfully insereted ......")

def HandleGet():
    data=col.find()
    for i in data:
        print(i)

def HandleDelete():
    col.delete_one({'name':'Test'})
    print("Deleted Sucessfully...")

def HandleUpdate():
    col.update_one({'name':'ram'},{'$set':{'name':'Xyz'}})
    print("data update sucessfully")


l= Label(root,text = "Enter name")
l.grid(row=0,column=1)
e1 =Entry(root)
e1.grid(row=0,column=2)
b1 = Button(root,text="Submit",command=HandleInsert)
b1.grid(row=1,column=2)
b2 = Button(root,text="Get",command=HandleGet)
b2.grid(row=2,column=2)
b3 = Button(root,text="Find",command=HandleGet)
b3.grid(row=3,column=2)
b4 = Button(root,text="Delete",command=HandleDelete)
b4.grid(row=4,column=2)
b5 = Button(root,text="Update",command=HandleUpdate)
b5.grid(row=5,column=2)


root.mainloop()