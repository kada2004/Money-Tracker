from tkinter import*
import tkinter as tk
import tkinter.messagebox as messagebox
root=Tk()
root.title("Money Tracker")
import pandas as pd
from datetime import datetime

main_label1=Label(root,text="Add Money")    
main_label1.grid(row=1,column=2,columnspan=2)


entry1=Entry(root)
entry1.grid(row=2,column=2,columnspan=2)


money=0
password_value=0

switch=0

revision_class_data=0
new_class_data=0
remain_money=0

def date_time():
    current_datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    main_label3.config(text=f"Date and Time :{current_datetime}")
    main_label3.after(1000,date_time)
    return current_datetime


def save_function():
    global switch
    switch=1

    
    
    password_window()
    
def save_value():
    global money
    global password_value

    if (password_value==True):

        money=int(entry1.get())
        main_label2.config(text=f"Remainning Money :{money}")
        entry1.delete(0,END)
        save_to_excel()

    else:
        entry1.delete(0,END)

        
def save_to_excel():

    path="C:\\Users\\DAN KALENGA\\OneDrive\Bureau\\Python Advanced\\money tracker dan classes.xlsx"

    current_datetime=date_time()
  
    data_list={"date and time":[current_datetime],"Total_money":[money],"Revision Class":[revision_class_data],"New Class":[new_class_data]}

    df=pd.DataFrame(data_list)

    try:
        existing_data=pd.read_excel(path)
        df=pd.concat([existing_data,df],ignore_index=True)
    except FileNotFoundError:
        pass
        

    df.to_excel(path,index=False)


def revision_class_func():
    global switch
    switch=2

    password_window()
   
    
def execute_revision_class():

    global password_value

    global money

    global revision_class_data

    global new_class_data

    if (password_value==True):


        revision_class_data=1

        new_class_data=0
    
        revision_class = 10
        revision_class_money=money-revision_class
        main_label2.config(text=f"Remainning Money :{revision_class_money}")
        money=revision_class_money
        save_to_excel()

def new_class_function():
    global switch
    switch=3
    password_window()

def execute_new_class():

    global password_value

    global money
    global revision_class_data

    global new_class_data

    if (password_value==True):

        revision_class_data=0

        new_class_data=1

        new_class=20
        new_class_remain_money=money-new_class
        main_label2.config(text=f"Remainning Money :{new_class_remain_money}")
        money=new_class_remain_money
        save_to_excel()

def password_window():

    window_1=tk.Toplevel(root)
    window_1.title("Password")
    window_1.geometry("200x100")
    main_label3=Label(window_1,text="Password")    
    main_label3.pack()

    entry1=Entry(window_1,show="*")
    entry1.pack()
    button4=Button(window_1,text="Submit",command=lambda: check_password(entry1.get(),window_1))
    button4.pack()

def check_password(typed_password,window_1):
    global password_value
    global switch 
    default_password="123"
  
    if (typed_password==default_password):
        messagebox.showinfo("Password info","Password is correct")
        password_value=True
        if(switch==1):
            save_value()
            switch=0
        if(switch==2):

            execute_revision_class()
           
            switch=0
        if(switch==3):
            execute_new_class()
          
            switch=0


    else:
        messagebox.showinfo("Password info","Password is incorrect")
        password_value=False
        save_value()
        
    window_1.destroy()

def read_data_function():
    path="C:\\Users\\DAN KALENGA\\OneDrive\Bureau\\Python Advanced\\money tracker dan classes.xlsx"

    window_2=tk.Toplevel(root)
    window_2.title("History")
    window_2.geometry("550x500")
    main_label4=Label(window_2,text="Output")    
    main_label4.pack()
    text_box=Text(window_2,width=65,height=25)
    text_box.pack()
    button5=Button(window_2,text="Erase",command=erase_function_from_excelsheet,width=20)
    button5.pack()
    
    existing_data=pd.read_excel(path)
    text_box.insert(END,existing_data)

def erase_function_from_excelsheet():
    pass 
    


def reading_last_entry_money_from_excel():
    global money
    path="C:\\Users\\DAN KALENGA\\OneDrive\Bureau\\Python Advanced\\money tracker dan classes.xlsx"
    existing_data=pd.read_excel(path)
    print(existing_data.columns.ravel())
    money_list=existing_data['Total_money'].tolist()
    print(money_list)
    last_money=money_list[-1]
    money=last_money
    main_label2.config(text=f"Remainning Money :{money}")

    

   
button1=Button(root,text="save",command=save_function,width=10)
button1.grid(row=3,column=2,columnspan=2)


button2=Button(root,text="Read Data",command=read_data_function,width=10)
button2.grid(row=4,column=2,columnspan=2)

button3=Button(root,text="Revision Class",command=revision_class_func,width=20)
button3.grid(row=5,column=2)

button4=Button(root,text="New Class",command=new_class_function,width=20)
button4.grid(row=5,column=3)



main_label2=Label(root,text="Remainning Money")    
main_label2.grid(row=6,column=2,columnspan=2)

main_label3=Label(root,text="Date and Time")    
main_label3.grid(row=7,column=2,columnspan=2)
current_datetime=date_time()

reading_last_entry_money_from_excel()

root.mainloop()