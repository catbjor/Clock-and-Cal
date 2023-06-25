from tkinter import *
from tkinter import ttk
from time import strftime
from tkcalendar import Calendar

root = Tk()
root.title("Spooky Time")
root.configure(bg="black")

def update_time():
    string = strftime('%H:%M:%S %p')
    time_label.config(text=string)
    time_label.after(1000, update_time)

def update_calendar():
    year = int(strftime('%Y'))
    month = int(strftime('%m'))
    cal_frame = Frame(root, bg="black")
    cal = Calendar(
        cal_frame,
        selectmode="day",
        background='black',
        foreground='white',
        bordercolor='none',
        headersbackground='black',
        normalbackground='black',
        normalforeground='white',
        weekendbackground='black',
        weekendforeground='white',
        othermonthbackground='black',
        othermonthforeground='gray',
        font=("Araslik", 25),
        showothermonthdays=False,
        selectbackground='orange',
        selectforeground='black'
    )
    cal.pack()
    cal_frame.pack(anchor='center')

time_label = Label(root, font=("Babilo", 80), background="black", foreground="orange")
time_label.pack(anchor='center', pady=20)

update_time()
update_calendar()

root.mainloop()
