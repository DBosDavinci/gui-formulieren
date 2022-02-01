from datetime import *
from calendar import monthrange
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.geometry("200x100")

maanden = ["Jan","Feb","Mar","Apr","Mei","Jun","Jul","Aug","Sep","Okt","Nov","Dec"]
today = date.today()
todayjaar = int(today.strftime("%Y"))
todaymaand = int(today.strftime("%m"))
todaydag = int(today.strftime("%d"))

Title = Label(root, text="Date:")
Title.place(relx=.5, rely=.1, anchor=N)

boxFrame = Frame(root)
boxFrame.place(relx=.5, rely=.5, anchor="center")

selected_day = StringVar()
days_cb = ttk.Combobox(boxFrame, textvariable=selected_day, width=5)
days_cb['values'] = [x for x in range(1, (monthrange(todayjaar, todaymaand)[1])+1)]
days_cb.current(todaydag-1)
days_cb['state'] = 'readonly'
days_cb.pack(side="left")

fillLabel1 = Label(boxFrame, text="-")
fillLabel1.pack(side="left")

def updateDaysMaand(self):
    maand = maanden.index(selected_month.get())+1
    jaar = int(selected_year.get())
    days_cb['values'] = [x for x in range(1, (monthrange(jaar, maand)[1])+1)]

selected_month = StringVar()
month_cb = ttk.Combobox(boxFrame, textvariable=selected_month, width=5)
month_cb['values'] = [maanden[m] for m in range(0, 12)]
month_cb.current(todaymaand-1)
month_cb.bind('<<ComboboxSelected>>', updateDaysMaand)
month_cb['state'] = 'readonly'
month_cb.pack(side="left")

fillLabel2 = Label(boxFrame, text="-")
fillLabel2.pack(side="left")

selected_year = StringVar()
year_entry = Entry(boxFrame, textvariable=selected_year, width=5)
year_entry.insert(0,todayjaar)
year_entry.pack(side="left")

def DaysFromDate():
    d0 = date.today()
    d1 = date(int((selected_year.get())),(maanden.index(selected_month.get())+1),int(selected_day.get()))
    delta = d1 - d0
    if delta.days > 0:
        messagebox.showinfo(message=f"Dit is {delta.days} dagen in de toekomst")
    elif delta.days < 0:
        messagebox.showinfo(message=f"Dit is {abs(delta.days)} dagen geleden")
    else:
        messagebox.showinfo(message="Dit is vandaag")
        
printButton=Button(root,text="go",command=DaysFromDate)
printButton.place(relx=.45, rely=.7)

root.mainloop()