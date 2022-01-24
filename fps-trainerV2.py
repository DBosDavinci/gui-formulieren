from tkinter import *
from random import randrange
from tkinter.messagebox import askyesno

root = Tk()

root.configure(bg="gray")
root.geometry("400x200")
challengeLabel = ""
challenge = ""
score=0
keys = ["w","a","s","d","space","Button","Double-Button","Triple-Button"]

def startButton():
    global start
    start = Button(text="press here to start",bd=0,command=bepaalTijd)
    start.place(relx = 0.5, rely = 0.5, anchor=CENTER)

def bepaalTijd():
    global email_entry,window
    window = Tk()
    window.geometry("100x100")
    window.title('')

    signin = Frame(window)
    signin.pack(padx=10, pady=10, fill='x', expand=True)

    email_label = Label(signin, text="Voer tijd in:")
    email_label.pack(fill='x', expand=True)

    email_entry = Entry(signin)
    email_entry.pack(fill='x', expand=True)
    email_entry.insert(0, "20")

    startButton = Button(signin, text="press here to start", command=getEntry)
    startButton.pack(fill='x', expand=True, pady=10)

def getEntry():
    global time, email_entry
    time = int(email_entry.get())
    startFunc()

def startFunc():
    global score,timeVar
    score=0
    window.destroy()
    start.destroy()
    countdown()
    createChallenge()

def countdown():
    global score,time,challengeLabel,challenge
    if time >= 1:
        label.config(text=f'Time remaining: {time}')
        time-=1
        root.after(1000, countdown)
    else:
        label.config(text=f'Time remaining: {time}')
        answer = askyesno(message=f"Congratulations you have {score} points, do you want to play again?")
        if answer:
            challengeLabel.destroy()
            root.unbind(f"<{challenge}>")
            bepaalTijd()
        else:
            root.destroy()

def createChallenge():
    global challenge, challengeLabel
    challenge = keys[randrange(0,8)]
    challengeLabel = Label(root,text=f"Press: {challenge}")
    root.bind(f"<{challenge}>",deleteLabel)
    challengeLabel.place(x=randrange(0,290),y=randrange(20,180))

def deleteLabel(self):
    global score,challengeLabel,challenge
    challengeLabel.destroy()
    root.unbind(f"<{challenge}>")
    if keys.index(challenge) in range(0,5):
        score+=1
        label1.configure(text=f'{score} points')
    elif keys.index(challenge) in range(5,8):
        score+=2
        label1.configure(text=f'{score} points')
    createChallenge()

startButton()

top = Frame(root)
top.pack(side=TOP,fill=X)

label = Label(text="Time remaining: 20",bg="black",fg="white",width=30,height=1)
label.pack(in_=top,side=LEFT)
label1 = Label(text="0 points",bg="black",fg="white",width=30,height=1)
label1.pack(in_=top,side=LEFT)

root.mainloop()