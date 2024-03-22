from tkinter import *
from tkinter import messagebox
from data import Database

win = Tk()
data = Database('e:/contact.db')

screen_w = win.winfo_screenwidth()
screen_h = win.winfo_screenheight()

cx = screen_w/2
cy = screen_h/2
ww = 680
wh = 400
wl = int(cx - ww/2)
wt = int(cy - wh/2)

win.geometry(f'{ww}x{wh}+{wl}+{wt}')
win.title('contact')

bg1 = '#e2f8ff'
win.config(bg = bg1)
fg1 = '#51056F'
#==========functions=============
def show():
    lst_data.delete(0,END)
    entry = data.fetch()
    for thing in entry:
        lst_data.insert(END,thing)
        
def insert():
    if ent_name.get() == '' or ent_fname.get() == '':
        messagebox.showerror('ERROR','Complete the stared field')
        
    if ent_name.get().isalpha() == FALSE:
        messagebox.showwarning('Warning','write the name in correct way')
        ent_name.delete(0,END)
        lbl_nameerror.config(text='have to be alphabet')
    else:
        name = ent_name.get()
        
    if ent_fname.get().isalpha() == FALSE:
        messagebox.showwarning('ERROR','write familyname in correct way')
        ent_fname.delete(0,END)
        lbl_fnameerror.config(text='have to be alphabet')
    else:
        fname = ent_fname.get()
        
    if len(ent_phone.get()) !=8 or ent_phone.get().isdigit() == FALSE:
        messagebox.showwarning('ERROR','enter phone number in correct way')
        ent_phone.delete(0,END)
        lbl_phoneerror.config(text='have to be 8 digit')
    else:
        phone = ent_phone.get()
        address = ent_address.get()
    data.insert(name, fname, address, phone)
    lbl_nameerror.config(text='')
    lbl_fnameerror.config(text='')
    lbl_phoneerror.config(text='')
    show()
    clear() 

def clear():
    ent_name.delete(0,END)
    ent_fname.delete(0,END)
    ent_address.delete(0,END)
    ent_phone.delete(0,END)
    ent_name.focus_set()    
        
def select(event):
    global selected
    index = lst_data.curselection()
    selected = lst_data.get(index)
    clear()
    ent_name.insert(END, selected[1])
    ent_fname.insert(END, selected[2])
    ent_address.insert(END, selected[3])
    ent_phone.insert(END, selected[4])

def delete():
    global selected
    result = messagebox.askquestion('Delete Data?',f'Do you want to delete {selected[0]}?')
    if result == 'yes':
        data.remove(selected[0])
        clear()
        show()

def edit():
    data.update(ent_name.get(), ent_fname.get(), ent_address.get(), ent_phone.get(), selected[0])
    clear()
    show()

def search():
    global selected
    lst_data.delete(0,END)
    row = data.search(ent_search.get())
    if row == None:
        messagebox.showerror('NOT FOUND','The searched item not found')
    else:
        for i in row:
            ent_search.delete(0,END)
            lst_data.insert(END,i)

def exit1():
    leave = messagebox.askquestion('EXIT','Do you want to leave this app?')
    if leave == 'yes':
        win.destroy()





#========UI DESIGN=====================
lbl_text = Label(win,text='Manage contacts',font='times 15 bold',bg = 'red' ,fg = 'white' )
lbl_text.place(x= 520 , y= 10)
lbl_star = Label(win,text='*',fg='red',bg=bg1,font='arial 25')
lbl_star.place(x=240 , y=55)
lbl_star = Label(win,text='*',fg='red',bg=bg1,font='arial 25')
lbl_star.place(x=530 , y=55)

search_text = StringVar()
search_text.set('search')
ent_search = Entry(win,textvariable=search_text,width=20)
ent_search.place(x= 20 , y = 15)

lbl_name = Label(win,text='Name:',font='TIMES 14 bold',bg = bg1,fg = fg1)
lbl_name.place(x = 40 , y=55)
ent_name = Entry(win,font='TIMES 12',width=15)
ent_name.place(x= 110 , y=60)
lbl_nameerror = Label(win,text='',font='TIMES 12 bold',bg=bg1,fg='red')
lbl_nameerror.place(x=110 , y=80)

lbl_fname = Label(win,text='Fname:',font='TIMES 14 bold',bg = bg1,fg = fg1)
lbl_fname.place(x = 325 , y= 55)
ent_fname = Entry(win,font='TIMES 12',width=15)
ent_fname.place(x= 400 , y=60)
lbl_fnameerror = Label(win,text='',font='TIMES 12 bold',bg=bg1,fg='red')
lbl_fnameerror.place(x=400 , y=80)

lbl_address = Label(win,text='Address:',font='TIMES 14 bold',bg = bg1,fg = fg1)
lbl_address.place(x = 25 , y= 110)
ent_address = Entry(win,font='TIMES 12',width=15)
ent_address.place(x= 110 , y=115)

lbl_phone = Label(win,text='Phone:',font='TIMES 14 bold',bg = bg1,fg = fg1)
lbl_phone.place(x = 330 , y= 110)
ent_phone = Entry(win,font='TIMES 12',width=15)
ent_phone.place(x= 400 , y=115)
lbl_phoneerror = Label(win,text='',font='TIMES 12 bold',bg=bg1,fg='red')
lbl_phoneerror.place(x=400 , y=135)

lst_data = Listbox(win,font='TIMES 14',width=35 , height=9)
lst_data.place(x=25 , y=160)
lst_data.bind('<<ListboxSelect>>',select)
sb = Scrollbar(win)
sb.place(x=350 , y=160, height=205)

btn_show = Button(win,text='Show list',font='TIMES 14 bold',fg='white',bg=fg1,width=10,command=show)
btn_show.place(x= 390 , y= 162)

btn_insert = Button(win,text='Insert',font='TIMES 14 bold',fg='white',bg=fg1,width=10,command=insert)
btn_insert.place(x= 530 , y= 162)

btn_edit = Button(win,text='Edit',font='TIMES 14 bold',fg='white',bg=fg1,width=10,command=edit)
btn_edit.place(x= 390 , y= 220)

btn_clear = Button(win,text='Clear',font='TIMES 14 bold',fg='white',bg=fg1,width=10,command=clear)
btn_clear.place(x= 530 , y= 220)

btn_delete = Button(win,text='Delete',font='TIMES 14 bold',fg='white',bg=fg1,width=10,command=delete)
btn_delete.place(x=390 , y= 280)

btn_exit = Button(win,text='Exit',font='TIMES 14 bold',fg='white',bg='#F02C2C',width=10,command=exit1)
btn_exit.place(x= 530 , y= 280)

btn_show = Button(win,text='🔎',font='TIMES 10 bold',command=search)
btn_show.place(x= 150 , y= 10)
win.mainloop()








