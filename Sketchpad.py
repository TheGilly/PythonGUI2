from tkinter import *

Screen = Tk()
Screen.geometry("800x800")
Screen.config(bg = "black")
Screen.title("Sketchpad")


lastX = None
lastY = None

penwidth = 0
pencolour = "black"

erasing = False 

def erase():
    global pencolour, erasing
    erasing = True
    pencolour = "white"
    


def paint(event):
    global penwidth, pencolour, erasing
    print(erasing)
    if erasing == True:
        pencolour = "white"
    else:
        selected_indices = L1.curselection()
        if selected_indices:
            first_index = selected_indices[0]
            pencolour = Colours[first_index]
        
    

    lastX = event.x
    lastY = event.y
    penwidth = Scale1.get()
    C1.create_line(lastX, lastY, event.x, event.y, width = penwidth, fill = pencolour, smooth = True, capstyle = "round")
    lastX = event.x
    lastY = event.y


def pen():
    global penwidth, erasing
    penwidth = 5
    erasing = False


def brush():
    global penwidth, erasing
    penwidth = 20
    erasing = False
    


    


PenButton = Button(text = "Pen", height = 1, width = 10, bg = "orange", fg = "red", font = (12), command = pen)
PenButton.place(x = 15, y = 30)

BrushButton = Button(text = "Brush", height = 1, width = 10, bg = "orange", fg = "red", font = (12), command = brush)
BrushButton.place(x = 150, y = 30)

EraserButton = Button(text = "Eraser", height = 1, width = 10, bg = "orange", fg = "red", font = (12), command = erase)
EraserButton.place(x = 300, y = 30)

PenWidthLabel = Label(text = "Pen Width", height = 1, width = 10, bg = "orange", fg = "red", font = (12))
PenWidthLabel.place(x = 450, y = 30)

Scale1 = Scale(from_ = 0, to = 100, orient = "horizontal", length = 200)
Scale1.place(x = 600, y = 30)

ColourLabel = Label(text = "Select your colour", height = 1, width = 18, bg = "orange", fg = "red", font = (12))
ColourLabel.place(x = 90, y = 80)

L1 = Listbox(width = 30, height = 3)
L1.place(x = 300, y = 80)

Colours = ["green", "yellow", "orange", "red", "black", "pink", "blue"]

for i in Colours:
    L1.insert(END, i)


C1 = Canvas(width = 800, height = 700, bg = "white")
C1.place(x = 0, y = 150)
C1.bind("<B1-Motion>", paint)







































Screen.mainloop()


