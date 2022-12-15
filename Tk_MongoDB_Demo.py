from tkinter import *
from pymongo import MongoClient
from tkinter import ttk, messagebox

# database
client = MongoClient("localhost", 27017)
db = client['student_db']
coll = db["student_data"]

set_var=False
def reset():
    name_E.delete(0, END)
    email_E.delete(0, END)
    age_E.delete(0, END)
    g.set(None)


def insert():
  global set_var
  name = tree.item(tree.selection())['values']
  if(email_E.get() != '' and g.get() != '' and name_E.get() != '' and set_var==False):
        if(g.get() == 1):
          getGender = 'Male'
        else:
          getGender = 'Female'
        coll.insert_one({'name': name_E.get(), 'email': email_E.get(),
                    'gender': getGender, 'age': age_E.get()})
        for data in tree.get_children():
          tree.delete(data)
        for i in coll.find():
          tree.insert("", END, values=[i['name'],
                    i['email'], i['gender'], i['age']])
        messagebox.showinfo('success', 'data inserted sucesfully')
        reset()
  
  elif name != '' and set_var==True:
      if(email_E.get() != '' and g.get() != '' and name_E.get() != ''): 
          if(g.get() == 1):
            getGender = 'Male'
          else:
            getGender = 'Female'

          coll.update_one({'name': name[0]}, {'$set': {'name': name_E.get(
          ), 'email': email_E.get(), 'gender': getGender, 'age': age_E.get()}})

          reset()

          for data in tree.get_children():
            tree.delete(data)
          for i in coll.find():
            tree.insert("", END, values=[
                        i['name'], i['email'], i['gender'], i['age']])
                        
          messagebox.showinfo('success', 'data updated sucesfully')
          set_var=False
      else:
          messagebox.showwarning('warning','please fill data')
  else:
        messagebox.showwarning('warning', 'please fill the data')

def update():
    global set_var
    name = tree.item(tree.selection())['values']
    if name != '':

      name = tree.item(tree.selection())['values']
      if(name_E.get()!=name[0]):
        name_E.insert(0, name[0])
        email_E.insert(0, name[1])
        age_E.insert(0, name[3])

        if(name[2] == 'Male'):g.set(1)
        else:g.set(2)

      set_var=True
    else:
        messagebox.showwarning('warning','please select the data')


def delete():
   name = tree.item(tree.selection())['values']
   if name != '':
      coll.delete_one({'name': name[0]})
      for data in tree.get_children():
         tree.delete(data)
      for i in coll.find():
         tree.insert("", END, values=[i['name'],
                     i['email'], i['gender'], i['age']])
      messagebox.showinfo('success','data deleted sucesfully')
   else:
    messagebox.showwarning('warning', 'please select the data from table')

root=Tk()
root.state('zoomed')

g=IntVar()

# frame1
f1=Frame(root)
f1.place(x=150,y=150)

# fram2
f2=Frame(f1)
f2.grid(row=4,column=2)


name_l=Label(f1,text='first name')
name_E=Entry(f1)

name_l.grid(row=0,column=0)
name_E.grid(row=0,column=2)

email_l=Label(f1,text='Email')
email_E=Entry(f1)

email_l.grid(row=2,column=0)
email_E.grid(row=2,column=2)

gender_l=Label(f1,text='Gender')
r1=Radiobutton(f2,text='male',variable=g,value=1)
r2=Radiobutton(f2,text='female',variable=g,value=2)

gender_l.grid(row=4,column=0)
r1.pack()
r2.pack()

age_l=Label(f1,text='age')
age_E=Entry(f1)

age_l.grid(row=6,column=0)
age_E.grid(row=6,column=2)

# buttons
b1=Button(root,text='submit',bg='yellow',command=insert)
b1.place(x=200,y=300)

b3=Button(root,text='update',bg='yellow',command=update)
b3.place(x=200,y=340)

b4=Button(root,text='delete',bg='yellow',command=delete)
b4.place(x=200,y=380)

# table
col=('name','email','gender','age')
tree=ttk.Treeview(root,height=20,columns=col,show='headings')
tree.heading('name',text='Name')
tree.heading('email',text='email')
tree.heading('gender',text='gender')
tree.heading('age',text='age')

# anchor data in column
tree.column('name',anchor=CENTER)
tree.column('email',anchor=CENTER)
tree.column('gender',anchor=CENTER)
tree.column('age',anchor=CENTER)


for data in tree.get_children():
        tree.delete(data)
for i in coll.find():
    tree.insert("",END,values=[i['name'],i['email'],i['gender'],i['age']])
    
tree.place(x=400,y=100)

root.mainloop()