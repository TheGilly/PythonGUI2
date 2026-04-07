from tkinter import *

window = Tk()
window.title("Multiplication Table")
window.configure(bg = "orange")
window.geometry("600x600")

def generatetable():
    number = int(entrynumber.get())
    for i in range(1,11):
      line = "{}x{}={}".format(number,i,number*i)
      l1.insert(i,line)
    

titlelabel = Label(text = "Multiplication Table", width = 25, height = 1, bg = "red",fg = "black", font = (12))
titlelabel.place(x = 100, y = 20)

enternumber = Label(text = "Enter the number here", width = 20, height = 2, bg = "red", fg = "black", font = (12))
enternumber.place(x = 30, y = 60)

entrynumber = Entry( width = 30, bg = "blue", fg = "black")
entrynumber.place(x = 300, y = 70)

generate = Button(text = "Generate", width = 15, bg = "red", fg = "black", command = generatetable)
generate.place(x = 200, y = 150)

l1 = Listbox(width = 40, height = 20)
l1.place(x = 200, y = 180)
