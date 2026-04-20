from tkinter import *

window = Tk()
window.title("Multiplication Table")
window.configure(bg = "orange")
window.geometry("600x600")

def generatetable():
    l1.delete(0,END)
    number = int(entrynumber.get())
    rangeV = int(numberrange.get())
    for i in range(1,rangeV + 1):
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

rangeselect = Label(text = "Select your range", width = 15, bg = "purple", fg = "black")
rangeselect.place(x = 100, y = 120)

numberrange = IntVar()


R1 = Radiobutton(text = "10", value = 10, variable = numberrange)
R1.place(x = 250, y = 120)

R2 = Radiobutton(text = "20", value = 20, variable = numberrange)
R2.place(x = 350, y = 120)

R3 = Radiobutton(text = "30", value = 30, variable = numberrange)
R3.place(x = 450, y = 120)
