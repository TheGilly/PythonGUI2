from tkinter import *
import random

def getresult(userchoice):
    computeroptions = ["Rock", "Paper", "Scissors"]
    computerchoice = random.choice(computeroptions)
    if computerchoice == userchoice:
        result = "It is a tie"
    if computerchoice == "Rock":
        if userchoice == "Paper":
            result = "You win!"
        if userchoice == "Scissors":
            result = "You lose!"
    if computerchoice == "Paper":
        if userchoice == "Rock":
            result = "You lose!"
        if userchoice == "Scissors":
            result = "You win!"
    if computerchoice == "Scissors":
        if userchoice == "Rock":
            result = "You win!"
        if userchoice == "Paper":
            result = "You lose!"
    resultlabel.config(text = result)
    playerlabel.config(text = "PlayerChoice:" + userchoice)
    computerlabel.config(text = "ComputerChoice:" + computerchoice)
            
            
    

window = Tk()
window.title("Rock-Paper-Scissors Game")
window.configure(bg = "white")
window.geometry("700x700")

titlelabel = Label(text = "Rock-Paper-Scissors Game", width = 40, height =3, bg = "red", fg = "blue", font = (16))
titlelabel.place(x = 100, y = 30)

rockbutton = Button(text = "Rock",width = 20, height = 2, bg = "red", command = lambda: getresult("Rock"))
paperbutton = Button(text = "Paper",width = 20, height = 2, bg = "blue", command =lambda: getresult("Paper")) 
scissorsbutton = Button(text = "Scissors",width = 20, height = 2, bg = "green", command = lambda: getresult("Scissors"))
rockbutton.place(x = 70, y = 150)
paperbutton.place(x = 270, y = 150)
scissorsbutton.place(x = 470, y = 150)

resultlabel = Label(text = "Result", width = 20, height =3, bg = "red", font = (20))
resultlabel.place(x = 270, y = 300)

playerlabel = Label(text = "PlayerChoice: ", width = 20, height =1, bg = "white", font = (10))
playerlabel.place(x = 100, y = 230)

computerlabel = Label(text = "ComputerChoice: ", width = 20, height =1, bg = "white", font = (10))
computerlabel.place(x = 400, y = 230)


