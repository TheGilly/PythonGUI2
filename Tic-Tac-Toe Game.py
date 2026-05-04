from tkinter import*
from tkinter import messagebox

Screen = Tk()
Screen.title("Tic-Tac-Toe Game")
Screen.configure(bg = "white")
Screen.geometry("600x600")

turn = "x"

def TicTacToe(ButtonID):
    global turn
    ButtonID.config(text = turn)
    
    if B1["text"] == B2["text"] ==B3["text"] != "":
        messagebox.showinfo("win", turn + " wins")
    if turn == "x":
        turn = "o"
    else:
        turn = "x"
        
    
    

B1 = Button(width = 25, height = 10, bg = "yellow", fg = "red", font=("Arial", 12), command=lambda: TicTacToe(B1) )
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
