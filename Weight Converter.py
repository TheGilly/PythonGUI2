from tkinter import *
window = Tk()
window.title("Weight converter")
window.configure(bg = "blue")
window.geometry("700x700")



def convert():
    kgs = float(weightentry.get("1.0", "end-1c"))
    grams = kgs * 1000
    pounds = kgs / 2.2
    ounces = kgs * 35.2
    gramslabel.config(text = str(grams) + " grams")
    poundslabel.config(text = str(pounds) + " pounds")
    ounceslabel.config(text = str(ounces) + " ounces")

    
    
                      
    

enterlabel = Label(text = "Enter the weight(In Kgs)", width = 20, height =2, bg = "red",fg = "green", font = (16)) 
enterlabel.place(x = 100, y = 50)

weightentry = Text(width = 20, height = 3, bg = "white", fg = "blue", font = (44))
weightentry.place(x = 400, y = 50)

convertbutton = Button(text = "Convert", width = 20, height = 2, bg = "red", command = convert)
convertbutton.place(x = 300, y = 150)

gramslabel = Label(text = "   In grams", width = 20, height = 2,bg = "red")
gramslabel.place(x = 100, y = 250)

ounceslabel = Label(text = "   In ounces", width = 20, height = 2,bg = "red")
ounceslabel.place(x = 300, y = 250)

poundslabel = Label(text = "   In pounds", width = 20, height = 2,bg = "red")
poundslabel.place(x = 500, y = 250)


