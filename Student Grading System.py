from tkinter import*
from tkinter import messagebox

Screen = Tk()
Screen.title("Student Grading Systeam")
Screen.configure(bg = "white")
Screen.geometry("600x800")

Percentage = 0
Grade = ""

def add_entry():
    global Percentage, Grade
    with open("Student Details.txt", "a") as file:
        file.write(str(Percentage))
        file.write(Grade)
        file.close()
        


def gradecalculate():
    global Percentage, Grade
    MathScore = int(entermaths.get())
    ScienceScore = int(enterscience.get())
    EnglishScore = int(enterEnglish.get())
    Grade = MathScore + ScienceScore + EnglishScore
    Percentage = (Grade / 300) * 100
    print (str(Grade))
    Result.insert(END,str(Percentage) + "%")
    if Percentage > 80:
        Grade = "A"
    if Percentage > 70 and Percentage < 80:
        Grade = "B"
    if Percentage < 70:
        Grade = "C"
    Result.insert(END, "\n")              
    Result.insert(END,str(Grade) + " is your grade")
    

titlelabel = Label(text = "Student Grading System", width = 20, height =3, bg = "red", fg = "black", font = (16))
titlelabel.place(x = 200, y = 50)

namelabel = Label(text = "Enter your name", width = 15, height = 1, bg = "red", fg = "black", font = (16))
namelabel.place(x = 30, y = 150)

entername = Entry(width = 25, bg = "red", fg = "black")
entername.place(x = 300, y = 150)

namemaths = Label(text = "Enter your Maths score", width = 25, height = 1, bg = "red", fg = "black", font = (16))
namemaths.place(x = 30, y = 250)

entermaths = Entry(width = 25, bg = "red", fg = "black")
entermaths.place(x = 350, y = 250)

namescience = Label(text = "Enter your Science score", width = 25, height = 1, bg = "red", fg = "black", font = (16))
namescience.place(x = 30, y = 350)

enterscience = Entry(width = 25, bg = "red", fg = "black")
enterscience.place(x = 350, y = 350)

nameEnglish = Label(text = "Enter your English score", width = 25, height = 1, bg = "red", fg = "black", font = (16))
nameEnglish.place(x = 30, y = 450)

enterEnglish = Entry(width = 25, bg = "red", fg = "black")
enterEnglish.place(x = 350, y = 450)

calculatebutton = Button(text = "Calculate Grade", width = 25, height = 1, bg = "red", fg = "black", font = (16), command = gradecalculate)
calculatebutton.place(x = 30, y = 550)

savebutton = Button(text = "Save Student Details", width = 25, height = 1, bg = "red", fg = "black", font = (16), command = add_entry)
savebutton.place(x = 400, y = 550)

Result = Text(width = 40, height = 8, bg = "red", fg = "black")
Result.place(x = 50, y = 650)

