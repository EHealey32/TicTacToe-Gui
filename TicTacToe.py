import tkinter
from tkinter import *
import tkinter.messagebox
from tkinter import Menu


# create a tkinter window
root = Tk() 

#Defining Key, Global Variables
playerTurn = 1            
 #Key Functions
def playerValue(buttonPressed):
    global playerTurn

    #Swapping From X to O
    if(buttonPressed == 1):
        if(playerTurn == 1):
            topLeft['text'] = "X"
            playerTurn = 0
        elif(playerTurn == 0):
            topLeft['text'] = "O"
            playerTurn = 1
    elif(buttonPressed == 2):
        if(playerTurn == 1):
            topMiddle['text'] = "X"
            playerTurn = 0
        elif(playerTurn == 0):
            topMiddle['text'] = "O"
            playerTurn = 1
    elif(buttonPressed == 3):
        if(playerTurn == 1):
            topRight['text'] = "X"
            playerTurn = 0
        elif(playerTurn == 0):
            topRight['text'] = "O"
            playerTurn = 1
    elif(buttonPressed == 4):
        if(playerTurn == 1):
            middleLeft['text'] = "X"
            playerTurn = 0
        elif(playerTurn == 0):
            middleLeft['text'] = "O"
            playerTurn = 1
    elif(buttonPressed == 5):
        if(playerTurn == 1):
            middleMiddle['text'] = "X"
            playerTurn = 0
        elif(playerTurn == 0):
            middleMiddle['text'] = "O"
            playerTurn = 1
    elif(buttonPressed == 6):
        if(playerTurn == 1):
            middleRight['text'] = "X"
            playerTurn = 0
        elif(playerTurn == 0):
            middleRight['text'] = "O"
            playerTurn = 1
    elif(buttonPressed == 7):
        if(playerTurn == 1):
            bottomLeft['text'] = "X"
            playerTurn = 0
        elif(playerTurn == 0):
            bottomLeft['text'] = "O"
            playerTurn = 1
    elif(buttonPressed == 8):
        if(playerTurn == 1):
            bottomMiddle['text'] = "X"
            playerTurn = 0
        elif(playerTurn == 0):
            bottomMiddle['text'] = "O"
            playerTurn = 1
    elif(buttonPressed == 9):
        if(playerTurn == 1):
            bottomRight['text'] = "X"
            playerTurn = 0
        elif(playerTurn == 0):
            bottomRight['text'] = "O"
            playerTurn = 1

    checkWin()
    return buttonPressed

def checkWin():
    #Defning Key Variables
    btnArray = [topLeft,topMiddle,topRight,middleLeft,middleMiddle,middleRight,bottomLeft,bottomMiddle,bottomRight]
    #Checking All Ways User Could Win
    if(topLeft['text'] == "X" and topMiddle['text'] == "X" and topRight['text'] == "X"):
        tkinter.messagebox.showinfo('Win Screen','Congrats Player 1! You have won!')
        #Reset Game
        for i,t in enumerate(btnArray):
            btnArray[i]['text'] = ""
    elif(topLeft['text'] == "O" and topMiddle['text'] == "O" and topRight['text'] == "O"):
        tkinter.messagebox.showinfo('Win Screen','Congrats Player 2! You have won!')
        #Reset Game
        for i,t in enumerate(btnArray):
            btnArray[i]['text'] = ""
    elif(middleLeft['text'] == "X" and middleMiddle['text'] == "X" and middleRight['text'] == "X" or middleLeft['text'] == "O" and middleMiddle['text'] == "O" and middleRight['text'] == "O"):
        tkinter.messagebox.showinfo('Win Screen','Congrats Player 1! You have won!')
        #Reset Game
        for i,t in enumerate(btnArray):
            btnArray[i]['text'] = ""
    elif(bottomLeft['text'] == "X" and bottomMiddle['text'] == "X" and bottomRight['text'] == "X" or bottomLeft['text'] == "O" and bottomMiddle['text'] == "O" and bottomRight['text'] == "O"):
        tkinter.messagebox.showinfo('Win Screen','Congrats Player 2! You have won!')
        #Reset Game
        for i,t in enumerate(btnArray):
            btnArray[i]['text'] = ""
    elif(topLeft['text'] == "X" and middleMiddle['text'] == "X" and bottomRight['text'] == "X" or topLeft['text'] == "O" and middleMiddle['text'] == "O" and bottomRight['text'] == "O"):
        tkinter.messagebox.showinfo('Win Screen','Congrats Player 1! You have won!')
        #Reset Game
        for i,t in enumerate(btnArray):
            btnArray[i]['text'] = ""
    elif(bottomLeft['text'] == "X" and middleMiddle['text'] == "X" and topRight['text'] == "X" or bottomLeft['text'] == "O" and middleMiddle['text'] == "O" and topRight['text'] == "O"):
        tkinter.messagebox.showinfo('Win Screen','Congrats Player 2! You have won!')
        #Reset Game
        for i,t in enumerate(btnArray):
            btnArray[i]['text'] = ""

    #Checking to see if they lost
    for i in btnArray:
        pass

#Creating root window configurations
root.geometry('800x700')
root.anchor("center")
root.title("Ethan's TicTacToe")
 
 #Creating Top Bar For Navigation
topMenu = Menu(root)

fileDropdown = Menu(topMenu)
helpDropdown = Menu(topMenu)

fileDropdown.add_command(label="New Game")
fileDropdown.add_command(label="Settings")
fileDropdown.add_command(label="Quit", command=root.destroy)

helpDropdown.add_command(label="Documentation")
helpDropdown.add_command(label="Tutorial")
helpDropdown.add_command(label="Follow me", command=lambda: print("Hello World"))

topMenu.add_cascade(label="File",menu=fileDropdown)
topMenu.add_cascade(label="Help", menu=helpDropdown)

root.config(menu=topMenu)
# Creating the buttons for the game
#Top Row Of Buttons
topLeft = Button(root, text="", height=7, width=10,command=lambda num=1: playerValue(num))
topMiddle = Button(root, text="", height=7, width=10, command=lambda num=2: playerValue(num))
topRight = Button(root, text="", height=7, width=10, command=lambda num=3: playerValue(num))

#Middle Row Of Buttons
middleLeft = Button(root, text="", height=7, width=10, bd = '5', command=lambda num=4: playerValue(num))
middleMiddle = Button(root, text="", height=7, width=10, bd = '5', command=lambda num=5: playerValue(num))
middleRight = Button(root, text="", height=7, width=10, bd = '5', command=lambda num=6: playerValue(num))

#Bottom Row of Buttons
bottomLeft = Button(root, text="", height=7, width=10, bd = '5', command=lambda num=7: playerValue(num))
bottomMiddle = Button(root, text="", height=7, width=10, bd = '5', command=lambda num=8: playerValue(num))
bottomRight = Button(root, text="", height=7, width=10, bd = '5', command=lambda num=9: playerValue(num))
 
#Grid For Button Elements
topLeft.grid(row=1)
topMiddle.grid(row=1, column=1)
topRight.grid(row=1,column=2)

middleLeft.grid(row=2)
middleMiddle.grid(row=2, column=1)
middleRight.grid(row=2,column=2)

bottomLeft.grid(row=3)
bottomMiddle.grid(row=3, column=1)
bottomRight.grid(row=3,column=2)
 
root.mainloop()