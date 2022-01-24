from tkinter import *

root = Tk()

for y in range(0,10):
    for x in range (0,10):
        if (y%2) == 0 and (x%2) == 0 or (y%2) != 0 and (x%2) != 0:
            test = Label(root,width=6,height=3,bg="black",fg="black")
            test.grid(column=x,row=y)
        else:
            test = Label(root,width=6,height=3,bg="white",fg="white")
            test.grid(column=x,row=y)

root.mainloop()