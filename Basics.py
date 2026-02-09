from tkinter import *
window = Tk()
window.title("Firstscreen")
window.configure(bg = "red")
window.geometry("700x700")
l1 = Label(text = "My SCreen", width = 20, height = 2,bg = "blue",fg = "green", font = (16))
l1.place(x = 200, y = 20)

l2 = Label(text = "Enter your name", width = 30, height =2,bg = "green",fg = "blue", font = (15))
l2.place(x = 55, y = 100)

E1 = Text(width = 20, height = 3, bg = "white", fg = "blue")
E1.place(x = 400, y = 100)

b1 = Button(text = "Submit", width = 20, height = 2, bg = "green", fg = "blue", font = (15))
b1.place(x= 200, y = 300)
