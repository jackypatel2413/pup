from pymongo import MongoClient
from tkinter import *
root=Tk()
root.geometry("300x300")
client=MongoClient("localhost",27017)
#db
database=client["student"]
#collection
col=database["student_info"]
#insert+
def HandleInsert():
    name=e1.get()
    col.insert_one({'name':name})
    e1.delete(0,END)
    print("Data sucessfully inserted........")


#to get values from collection
def HandleGet():
    data=col.find()
    for i in data:
        print(i)

#to delete value from collection
def HandleDelete():
    col.delete_one({'name':'Test'})
    print("Deleted Sucessfully...")

def HandleUpdate():
    col.update_one({'name':'ram'},{'$set':{'name':'Xyz'}})
    print("data updated sucessfully")

l=Label(root,text="Enter Name")
l.grid(row=0,column=1)
e1=Entry(root)
e1.grid(row=0,column=2)
b1=Button(root,text="Submit",command=HandleInsert)
b1.grid(row=1,column=2)
b2=Button(root,text="Get",command=HandleGet)
b2.grid(row=2,column=2)
b3=Button(root,text="Delete",command=HandleDelete)
b3.grid(row=3,column=2)
b4=Button(root,text="Update",command=HandleUpdate)
b4.grid(row=4,column=2)
root.mainloop()