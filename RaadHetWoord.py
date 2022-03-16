from tkinter import *
import string
from random import *

def startWindow():
    global woordlist, totalpoints, start
    start = Tk()

    woord = StringVar()
    entry = Entry(start, textvariable=woord)
    entry.pack()

    button = Button(start, text="Stel woord in", command=nieuwscherm)
    button.pack()

    woordlist = list(woord.get())
    totalpoints = len(woordlist)*len(woordlist)

    start.mainloop()

def generateLetter(x):
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)
    letter = alphabet_list[randrange(len(alphabet_list))]
    if letter not in x:
        x.append(letter)
    else:
        generateLetter(x)

def nieuwscherm():
    global letterdict
    
    if len(woordlist) >= 4 and len(woordlist) <= 7:
        start.destroy()
        guessword = Tk()
        letterdict = {}
        for x in range(len(woordlist)):
            letterlist = [woordlist[x]]
            for y in range(4):
                generateLetter(letterlist)
            shuffle(letterlist)
            spinbox = Spinbox(guessword, values=letterlist)
            letterdict[x] = spinbox
            spinbox.pack()
        button = Button(guessword, command=printVar)
        button.pack()

        guessword.mainloop()

def printVar():
    points = totalpoints
    goedeletters = len(letterdict)
    for x in range(len(letterdict)):
        if letterdict[x].get() != woordlist[x]:
            goedeletters-=1
            points-=2
    print(goedeletters,"letters goed")
    print(points)

startWindow()