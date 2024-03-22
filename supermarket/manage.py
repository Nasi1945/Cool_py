from tkinter import *
from tkinter import messagebox
from db import Database

win = Tk()
db = Database('e:/supermarket.db')
screen_w = win.winfo_screenwidth()
screen_h = win.winfo_screenheight()

cx = screen_w/2
cy = screen_h/2
ww = 650
wh = 350
wl = int(cx - ww/2)
wt = int(cy - wh/2)

win.geometry(f'{ww}x{wh}+{wl}+{wt}')
bg1 = '#D2D2DB'
win.config(bg = bg1)
win.title('مدیریت کتابخانه')

#=========function===============
def add():
    db.insert(ent_name.get(), ent_buy.get(), ent_sell.get(), ent_numbers.get())
    populate()
    clear()
    
def clear():
    ent_name.delete(0,END)
    ent_buy.delete(0,END)
    ent_sell.delete(0,END)
    ent_numbers.delete(0,END)
    ent_name.focus_set()

def select(event):
    global selected_item
    index = lst_devices.curselection()
    selected_item = lst_devices.get(index)
    clear()
    ent_name.insert(END,selected_item[1])
    ent_buy.insert(END,selected_item[2])
    ent_sell.insert(END, selected_item[3])
    ent_numbers.insert(END, selected_item[4])

def search():
    lst_devices.delete(0,END)
    row = db.search(ent_name.get(),ent_buy.get(),ent_sell.get(),ent_numbers.get())
    if row == None:
        messagebox.showerror('یافت نشد','مورد سرچ شده یافت نشد')
    else:
        for i in row:
            clear()
            lst_devices.insert(END,i)
       
def populate():
    lst_devices.delete(0,END)
    data = db.fetch()
    for things in data:
        lst_devices.insert(END, things)

def delete():
    global selected_item
    result = messagebox.askquestion('اخطار','آیا میخواهید مورد انتخاب شده حذف شود؟')
    if result == 'yes':
        db.remove(selected_item[0])
        clear()
        populate()

def update():
    global selected_item
    db.update(selected_item[0], ent_name.get(), ent_buy.get(),
              ent_sell.get(), ent_numbers.get())
    clear()
    populate()


def exit1():
    exit_1 = messagebox.askquestion('خروج','ایا میخواهید از برنامه خارج شوید؟')
    if exit_1 == 'yes':
        win.destroy()



#=======UI DESIGN================
lbl_name = Label(win,text='نام کالا : ',font='TIMES 14 bold',fg='red',bg = bg1)
lbl_name.place(x = 20 , y = 20)
ent_name = Entry(win,font='TIMES 12')
ent_name.place(x = 110 , y = 20)

lbl_buy = Label(win,text='قیمت خرید : ',font='TIMES 14 bold',fg='red',bg = bg1)
lbl_buy.place(x = 320 , y = 20)
ent_buy = Entry(win,font='TIMES 12')
ent_buy.place(x = 420 , y = 20)

lbl_sell = Label(win,text='قیمت فروش : ',font='TIMES 12 bold',fg='red',bg = bg1)
lbl_sell.place(x = 5 , y = 60)
ent_sell = Entry(win,font='TIMES 12')
ent_sell.place(x = 110 , y = 60)

lbl_numbers = Label(win,text='تعداد : ',font='TIMES 14 bold',fg='red',bg = bg1)
lbl_numbers.place(x = 340 , y = 60)
ent_numbers = Entry(win,font='TIMES 12')
ent_numbers.place(x = 420 , y = 60)

lst_devices = Listbox(win,font='TIMES 12',width=50,height=11)
lst_devices.place(x = 20 , y = 100)
lst_devices.bind('<<ListboxSelect>>',select)

sb = Scrollbar(win)
sb.place(x = 430 , y = 102,height=221)

btn_show = Button(win,text='نمایش لیست',font='TIMES 12 bold',width=15,command=populate)
btn_show.place(x = 470 , y=100)

btn_add = Button(win,text='اضافه کردن',font='TIMES 12 bold',width=15,command=add)
btn_add.place(x = 470 , y=140)

btn_search = Button(win,text='جستجوی کالا ',font='TIMES 12 bold',width=15,command=search)
btn_search.place(x = 470 , y=180)

btn_delete = Button(win,text='حذف کالا',font='TIMES 12 bold',width=15,command=delete)
btn_delete.place(x = 470 , y=220)

btn_update = Button(win,text='ویرایش',font='TIMES 12 bold',width=15,command=update)
btn_update.place(x = 470 , y=260)

btn_close = Button(win,text='بستن',font='TIMES 12 bold',width=15,command=exit1)
btn_close.place(x = 470 , y=300)
win.mainloop()








