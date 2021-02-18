from tkinter import *
from tkinter import Tk
from database_operation import *
from tkinter import font
from tkinter import messagebox
# root['font']=ff

root=Tk()
def save_contact():
    global num_entry,name_entry,addr_entry
    write_to_base(name_entry.get(),num_entry.get(),addr_entry.get())
    name_entry['text']=''
    num_entry['text'] =''
    addr_entry['text']=''
    messagebox.showinfo("Success","Contact details saved!")

def view_contact():
    global num_view_entry
    res=fetch_by_name(num_view_entry.get())
    num_del_entry['text']=''
    number=[]
    for x in res:
        number.append(x[1])
    s='\n'.join(number)
    ans_label['text']=s
    ans_label.pack()

def del_contact():
    global num_del_entry
    del_from_base(num_del_entry.get())
    num_del_entry['text']=''
    messagebox.showinfo("Success", "Contact details Deleted!")

def exit_func():
    sys.exit(0)


ff=font.Font(size=20)
heading=font.Font(size=25)
root.title("Contact Book")
root.geometry("400x600")
f1,f2,f3,f4=Frame(root),Frame(root),Frame(root),Frame(root)
head_label=Label(root,text="New Contact")
head_label.pack()
head_label['font']=heading
f1.pack()
save_btn=Button(root,text="save contact",font=ff,command=save_contact)
save_btn.pack()
nxt_label=Label(root,text="View Contact")
nxt_label.pack()
nxt_label['font']=heading
f2.pack()
view_btn=Button(root,text="View contact",font=ff,command=view_contact)
view_btn.pack()
del_label=Label(root,text="Delete Contact")
del_label.pack()
del_label['font']=heading
f3.pack()
del_btn=Button(root,text="Delete",font=ff,command=del_contact)
del_btn.pack()
f4.pack()
# F1 is a frame for saving contacts
name_label=Label(f1,text="Name:",font=ff)
name_label.grid(row=0,column=0)
name_entry=Entry(f1,font=ff)
name_entry.grid(row=0,column=1)

num_label=Label(f1,text="Number:",font=ff)
num_label.grid(row=1,column=0)
num_entry=Entry(f1,font=ff)
num_entry.grid(row=1,column=1)

addr_label=Label(f1,text="Address:",font=ff)
addr_label.grid(row=2,column=0)
addr_entry=Entry(f1,font=ff)
addr_entry.grid(row=2,column=1)


# F2 is for viewing contacts

f2_label=Label(f2,text="Name : ",font=ff)
f2_label.grid(row=0,column=0)
num_view_entry=Entry(f2,font=ff)
num_view_entry.grid(row=0,column=1)

f3_label=Label(f3,text="Number : ",font=ff)
f3_label.grid(row=0,column=0)
num_del_entry=Entry(f3,font=ff)
num_del_entry.grid(row=0,column=1)
ans_label=Label(f4,text="",font=ff)
ans_label.pack()
exit_btn=Button(f4,text="exit app",font=ff,command=exit_func)
exit_btn.pack()



root.mainloop()