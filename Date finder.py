import datetime
from tkinter import*

window = Tk()
window.title("date finder")
window.configure(bg = "orange")
window.geometry("400x400")

def getdate():
    a = datetime.datetime.now()
    b = a.strftime("%Y:%b:%d")
    date.config(text = b)

    

datefinder = Label(text = "Date", width = 15, height = 1, bg = "blue", fg = "black", font = (12))
datefinder.place(x = 70, y = 50)
showdate = Button(text = "Show date", width = 15, height = 1, bg = "red", fg = "black", font = (12),command =  getdate)
showdate.place(x = 70, y = 150)


date = Label(width = 15, height = 2, bg = "blue", fg = "black", font = (12))
date.place(x = 70, y = 220)
