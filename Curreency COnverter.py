from tkinter import *
window = Tk()
window.title("Currency converter")
window.configure(bg = "blue")
window.geometry("700x700")


def convert():
    euros = float(currencyentry.get("1.0", "end-1c"))
    rupees = euros * 92
    rupeeslabel.config(text = str(rupees) + " rupees")





enterlabel = Label(text = "Enter the amount of money(In Euros)", width = 40, height = 2, bg = "red", fg = "green", font = (16))
enterlabel.place(x = 60, y = 50)

currencyentry = Text(width = 20, height = 3, bg = "white", fg = "blue", font = (44))
currencyentry.place(x = 470, y = 50)

convertbutton = Button(text = "Convert", width = 20, height = 2, bg = "red", command = convert)
convertbutton.place(x = 300, y = 150)

rupeeslabel = Label(text = "   In rupees", width = 20, height = 2,bg = "red")
rupeeslabel.place(x = 100, y = 250)







