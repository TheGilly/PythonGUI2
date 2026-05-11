from tkinter import*
from tkinter import messagebox

Screen = Tk()
Screen.title("Tic-Tac-Toe Game")
Screen.configure(bg = "white")
Screen.geometry("600x600")

turn = "x"

turns = 0

iswin = False

def TicTacToe(ButtonID):
    global turn, turns, iswin
    ButtonID.config(text = turn)
    turns = turns + 1
    if B1["text"] == B2["text"] ==B3["text"] != "":
        messagebox.showinfo("win", turn + " wins")
        iswin = True
    

    if B4["text"] == B5["text"] ==B6["text"] != "":
        messagebox.showinfo("win", turn + " wins")
        iswin = True

    if B7["text"] == B8["text"] ==B9["text"] != "":
        messagebox.showinfo("win", turn + " wins")
        iswin = True

    if B1["text"] == B4["text"] ==B7["text"] != "":
        messagebox.showinfo("win", turn + " wins")
        iswin = True
    
    if B2["text"] == B5["text"] ==B8["text"] != "":
        messagebox.showinfo("win", turn + " wins")
        iswin = True
    

    if B3["text"] == B6["text"] ==B9["text"] != "":
        messagebox.showinfo("win", turn + " wins")
        iswin = True
    

    if B1["text"] == B5["text"] ==B9["text"] != "":
        messagebox.showinfo("win", turn + " wins")
        iswin = True
    

    if B3["text"] == B5["text"] ==B7["text"] != "":
        messagebox.showinfo("win", turn + " wins")
        iswin = True

    if turns == 9 and iswin == False:
        messagebox.showinfo("draw", "Its a tie")

    if turn == "x":
        turn = "o"
    else:
        turn = "x"
        
    
        
    
    

B1 = Button(width = 25, height = 10, bg = "yellow", fg = "red", font=(60), command=lambda: TicTacToe(B1) )
B1.place(x = 0, y = 0)


B2 = Button(width = 25, height = 10, bg = "yellow",font = (60), fg = "red",command=lambda: TicTacToe(B2) )
B2.place(x = 200, y = 0)

B3 = Button(width = 25, height = 10, bg = "yellow", font = (60),fg = "red",command=lambda: TicTacToe(B3) )
B3.place(x = 400, y = 0)

B4 = Button(width = 25, height = 10, bg = "yellow",font = (60), fg = "red",command=lambda: TicTacToe(B4) )
B4.place(x = 0, y = 200)

B5 = Button(width = 25, height = 10, bg = "yellow",font = (60), fg = "red",command=lambda: TicTacToe(B5) )
B5.place(x = 200, y = 200)

B6 = Button(width = 25, height = 10, bg = "yellow",font = (60), fg = "red",command=lambda: TicTacToe(B6) )
B6.place(x = 400, y = 200)

B7 = Button(width = 25, height = 10, bg = "yellow",font = (60), fg = "red",command=lambda: TicTacToe(B7) )
B7.place(x = 0, y = 400)

B8 = Button(width = 25, height = 10, bg = "yellow",font = (60), fg = "red",command=lambda: TicTacToe(B8) )
B8.place(x = 200, y = 400)

B9 = Button(width = 25, height = 10, bg = "yellow",font = (60), fg = "red",command=lambda: TicTacToe(B9) )
B9.place(x = 400, y = 400)
