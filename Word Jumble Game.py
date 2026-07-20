from tkinter import *
import random
from tkinter import messagebox


Riddles = {"What comes down but never goes up?":"Rain",  "What word contains 26 letters but only has three syllables?":"Alphabet", "What has a head but no brain?":"Lettuce", "What is more useful when it is broken?":"Egg", "The more you take, the more you leave behind. What am I?":"Footsteps"} 

questions = []
for i in Riddles.keys():
    questions.append(i)
currentquestion = questions[0]
currentanswer = ""
count = 0
score = 0

def start_game():
    global currentquestion, questions, Riddles, currentanswer, count
    count = count + 1
    QuestionLabel.config(text = currentquestion)
    currentanswer = Riddles[currentquestion]
    AnswerList = list(currentanswer)
    random.shuffle(AnswerList)
    shuffledanswer = "".join(AnswerList)
    AnswerLabel.config(text = shuffledanswer)
    if count == 5:
        NextButton.config(state = "disabled")
        


def next_question():
    global currentquestion, questions, Riddles, currentanswer, count, score
    
    
    youranswer = entrybox.get()
    if youranswer.lower() == currentanswer.lower():
        messagebox.showinfo("Correct", "You entered the right answer")
        score = score + 1
    else:
        messagebox.showinfo("Incorrect","You entered the wrong answer")
    entrybox.delete(0,END)
    nextindex = questions.index(currentquestion) + 1
    currentquestion = questions[nextindex]
    currentanswer = Riddles[currentquestion]
    start_game()

def submit_game():
    global score
    messagebox.showinfo("Result","Your score out of 5 is "+str(score)) 
    
    
    

Screen = Tk()
Screen.title("Word Jumble Game")
Screen.configure(bg = "white")
Screen.geometry("1000x1000")

Titlelabel = Label(text = "Word Jumble Game", width = 30, height = 3, bg = "blue", fg = "red", font = (16))
Titlelabel.place(x = 100, y = 20)

QuestionLabel = Label(text = "", width = 50, height = 2, bg = "black", fg = "red", font = (16))
QuestionLabel.place(x = 100, y = 100)

AnswerLabel = Label(text = "", width = 50, height = 2, bg = "black", fg = "red", font = (16))
AnswerLabel.place(x = 100, y = 200)

StartButton = Button(text = "Start", width = 15, height = 2, bg = "green", fg = "red", font = (16), command = start_game)
StartButton.place(x = 20, y = 400)

NextButton = Button(text = "Next", width = 15, height = 2, bg = "yellow", fg = "red", font = (16), command = next_question)
NextButton.place(x = 220, y = 400)

SubmitButton = Button(text = "Submit", width = 15, height = 2, bg = "blue", fg = "red", font = (16), command = submit_game)
SubmitButton.place(x = 420, y = 400)

entrybox = Entry(width = 30, bg = "white", fg = "black")
entrybox.place(x = 100, y = 300)
