from tkinter import*
import random
from tkinter import messagebox

actualnumber = random.randint(1,20)

turns = 0

def checkanswer():
    global turns
    turns += 1
    if turns > 5:
        message = "You have lost all of your lives. Game Over"
        messagebox.showinfo("result", message)
        return
    global actualnumber
    answer = int(enternumber.get("1.0", END))
    if actualnumber > answer:
        message = "Go higher!"
    if actualnumber < answer:
        message  = "Go lower!"
    if actualnumber == answer:
        message = "You are correct!"
    messagebox.showinfo("result", message)
    

window = Tk()
window.title("Guess the number")
window.configure(bg = "green")
window.geometry("800x800")

titlelabel = Label(text = "Welcome to the number guessing game!", width = 40, height = 4, bg = "red", font = (20))
titlelabel.place(x = 150, y = 50)

guesslabel = Label(text = "Guess a number from 1-20", width = 30, height = 3, bg = "purple", font = (20))
guesslabel.place(x = 50, y = 250)

enternumber = Text(width = 20, bg = "white", height = 3)
enternumber.place(x = 400, y = 250)

submit = Button(text ="Submit", width = 30, height = 3, bg = "yellow", font = (20), command = checkanswer)
submit.place(x = 200, y = 350)


