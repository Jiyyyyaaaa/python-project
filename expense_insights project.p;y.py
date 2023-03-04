from tkinter import * 
import tkinter.messagebox as mb
from tkinter.simpledialog import askinteger, askstring 
import tkinter.ttk as ttk
# from typing import Self  
import db

root = Tk()

##################### FUNCTIONS #############################
def add_another_expense():
   global date, payee, desc, amnt, MoP
   if not date.get() or not payee.get() or not desc.get() or not amnt.get() or not MoP.get():
        mb.showwarning("Error...!!","Please fill all the missing fields before pressing the add button!")
   else:
      print(date.get(),payee.get(), desc.get(), amnt.get(), MoP.get())
      db.insert_expense(date.get(),payee.get(), desc.get(), amnt.get(), MoP.get())
      mb.showinfo("Expense info", 'Expense added Successfully into the table!!')

def total_sum():
      global sum
      sum = db.show_total()
      Label(root, text="₹" , font=('Engravers MT', 18, 'bold'), bg='orange').place(x=650, y=90)
      Label(root, text=sum , font=('Engravers MT', 18, 'bold'), bg='orange').place(x=670, y=90)
      
def show():
         input_record()
         

def remove_expense():
   if not date.get() or not payee.get() or not desc.get() or not amnt.get() or not MoP.get():
          mb.showwarning('No record selected!', 'Please select a record to delete!')
   else:
        global remove_data
        remove_data = askinteger('Remove Expense', 'Which Expense you want to remove?')
        db.remove(remove_data)
        mb.showinfo('Expense Removed....!!', 'Hi, Expense is removed from Expense list {}'.format(remove_data))
        show()

def remove_all():
         mb.askyesno('Remove All Data','Are you sure you want to delete all expenses!')
         db.remove_all_db()
         mb.showinfo('Deleted','All Expense Data gone...!! Please click on "Show all Expenses" button to check')

   #exit function = 89

#########################################################################


################### GUI ##########################################

dataentery_frame_bg = 'Orange'
buttons_frame_bg = 'Black'
hlb_btn_bg = 'White'

lbl_font = ('Elephant', 12)
entry_font = ('Times 13 bold')
btn_font = ('Gill Sans MT', 12)

# root = Tk()
root.title('PythonGeeks Expense Insights')
root.geometry('1200x550')
root.resizable(0, 0)
Label(root, text='EXPENSE INSIGHTS', font=('Engravers MT', 18, 'bold'), bg='orange').pack(side=TOP, fill=X)

desc = StringVar()
amnt = DoubleVar()
payee = StringVar()
MoP = StringVar(value='Cash') 
date = StringVar() 

data_entry_frame = Frame(root, bg=dataentery_frame_bg)
data_entry_frame.place(x=0, y=30, relheight=0.95, relwidth=0.25)

buttons_frame = Frame(root, bg=buttons_frame_bg)
buttons_frame.place(relx=0.25, rely=0.05, relwidth=0.75, relheight=0.21)

tree_frame = Frame(root)
tree_frame.place(relx=0.25, rely=0.26, relwidth=0.75, relheight=0.74)

Label(data_entry_frame, text='Date (M/DD/YY)\t :', font=lbl_font, bg=dataentery_frame_bg).place(x=10, y=20)
GUI_DATE=Entry(data_entry_frame, font=entry_font, width=31, text=date).place(x=10, y=50)

Label(data_entry_frame, text='Payee\t             :', font=lbl_font, bg=dataentery_frame_bg).place(x=10, y=230)
GUI_PAYEE=Entry(data_entry_frame, font=entry_font, width=31, text=payee).place(x=10, y=260)

Label(data_entry_frame, text='Description           :', font=lbl_font, bg=dataentery_frame_bg).place(x=10, y=100)
GUI_DESC=Entry(data_entry_frame, font=entry_font, width=31, text=desc).place(x=10, y=130)

Label(data_entry_frame, text='Amount    ₹:\t         ', font=lbl_font, bg=dataentery_frame_bg).place(x=10, y=180)
GUI_AMT=Entry(data_entry_frame, font=entry_font, width=20, text=amnt).place(x=120, y=180)

Label(data_entry_frame, text='Mode of Payment:', font=lbl_font, bg=dataentery_frame_bg).place(x=10, y=310)
dd1 = OptionMenu(data_entry_frame, MoP, *['Cash'])
dd1.place(x=160, y=305)     ;     dd1.configure(width=10, font=entry_font)

Button(data_entry_frame, text='Add expense', command=add_another_expense, font=btn_font, width=30,bg=hlb_btn_bg).place(x=10, y=395)

# Button(data_entry_frame, text='Clear all Fields', command=lambda:date_textfield.delete(1.0,END), font=btn_font, width=30,bg=hlb_btn_bg).place(x=10, y=450)

Button(buttons_frame, text='Remove Expense', command=remove_expense, font=btn_font, width=25, bg=hlb_btn_bg).place(x=30, y=5)

Button(buttons_frame, text='Remove All Expenses',command=remove_all, font=btn_font, width=25, bg=hlb_btn_bg).place(x=335, y=5)

Button(buttons_frame, text='Exit', command=root.destroy, font=btn_font, width=25, bg=hlb_btn_bg).place(x=640, y=5)

Button(buttons_frame, text='Total Expense', command=total_sum, font=btn_font, width=25, bg=hlb_btn_bg).place(x=30, y=65)

Button(buttons_frame, text='Show All Expenses', command=show, font=btn_font, width=25, bg=hlb_btn_bg).place(x=640, y=65)

table = ttk.Treeview(tree_frame, selectmode=BROWSE, columns=('ID', 'Date', 'Payee', 'Description', 'Amount', 'Mode of Payment'))
X_Scroller = Scrollbar(table, orient=HORIZONTAL, command=table.xview)
Y_Scroller = Scrollbar(table, orient=VERTICAL, command=table.yview)
X_Scroller.pack(side=BOTTOM, fill=X)
Y_Scroller.pack(side=RIGHT, fill=Y) 

table.config(yscrollcommand=Y_Scroller.set, xscrollcommand=X_Scroller.set)

table.heading('ID', text='S No.', anchor=CENTER)
table.heading('Date', text='Date', anchor=CENTER)
table.heading('Payee', text='Payee', anchor=CENTER)
table.heading('Description', text='Description', anchor=CENTER)
table.heading('Amount', text='Amount', anchor=CENTER)
#table.heading('Mode of Payment', text='Mode of Payment', anchor=CENTER)

# table.column('#0', width=0, stretch=YES)
# table.column('#1', width=50, stretch=YES)
table.column('#0', width=180, stretch=YES)  # SR.NO column
table.column('#1', width=30, stretch=YES)  # Date column
table.column('#2', width=60, stretch=YES)  # Payee column
table.column('#3', width=90, stretch=YES)  # Title column
table.column('#4', width=120, stretch=YES)  # Amount column
# table.column('#5', width=150, stretch=YES)  # Mode of Payment column
table.place(relx=0, y=0, relheight=1, relwidth=1)
   
def input_record():
   table.insert('','end',text='Current Data is here below:')
   global sql_data
   sql_data=db.show_data()
   # table.insert(parent='',index='end',text='',values=('###New Data is here below:#####'))
   for i in sql_data:
        sub_list=i
        for j in sub_list:
                 global date,payee,desc,amt,mop
                 date=[sub_list[0]]
                 payee=[sub_list[1]]
                 desc=[sub_list[2]]
                 amt=[sub_list[3]]
                 mop=[sub_list[4]]
                 
        table.insert(parent='',index='end',text='',values=(date,payee,desc,amt,mop))

root.update()
root.mainloop()
