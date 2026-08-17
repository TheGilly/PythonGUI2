from tkinter import *
from tkinter import messagebox
Screen = Tk()
Screen.configure(bg = "white")
Screen.geometry("800x800")
Screen.title("Address Book")


def add_details():
    name = NameEntry.get()
    address = AddressEntry.get("1.0","end-1c")
    mobile = MobileEntry.get()
    email = EmailEntry.get()
    birthday = BirthdayEntry.get()
    file = open("Address Book.txt", "a")
    result = "Name: " + name + " Address: " + address + " Mobile: " + mobile + " Email: " + email + " Birthday: " + birthday
    file.write(result)
    file.write("\n")
    file.close()
    messagebox.showinfo("Details", "Your entry has been saved")

def open_details():
    Listbox1.delete(0, END)
    file = open("Address Book.txt", "r")
    Filecontent = file.read()
    entries = Filecontent.split("\n")
    print(entries)
    for i in entries:
        Listbox1.insert(END, i)
    file.close()  



Titlelabel = Label(text = "My Address Book", width = 20, height = 3, bg = "yellow", fg = "brown", font = (16))
Titlelabel.place(x = 200, y = 50)

Openbutton = Button(text = "Open", width = 15, height = 3, bg = "white", fg = "black", command = open_details)
Openbutton.place(x = 500, y = 50)

Namelabel = Label(text = "Name:", width = 15, height = 3, bg = "yellow", fg = "brown", font = (16))
Namelabel.place(x = 300, y = 200)

Addresslabel = Label(text = "Address:", width =15, height = 3, bg = "yellow", fg = "brown", font = (16))
Addresslabel.place(x = 300, y = 300)

Mobilelabel = Label(text = "Mobile:", width = 15, height = 3, bg = "yellow", fg = "brown", font = (16))
Mobilelabel.place(x = 300, y = 400)

Emaillabel = Label(text = "Email:", width = 15, height = 3, bg = "yellow", fg = "brown", font = (16))
Emaillabel.place(x = 300, y = 500)

Birthdaylabel = Label(text = "Birthday", width = 15, height = 3, bg = "yellow", fg = "brown", font = (16))
Birthdaylabel.place(x = 300, y = 600)

NameEntry = Entry(width = 25,  bg = "white", fg = "black")
NameEntry.place(x = 500, y = 200)

AddressEntry = Text(width = 25, height = 3, bg = "white", fg = "black")
AddressEntry.place(x = 500, y = 300)

MobileEntry = Entry(width = 25,  bg = "white", fg = "black")
MobileEntry.place(x = 500, y = 400)

EmailEntry = Entry(width = 25,  bg = "white", fg = "black")
EmailEntry.place(x = 500, y = 500)

BirthdayEntry = Entry(width = 25,  bg = "white", fg = "black")
BirthdayEntry.place(x = 500, y = 600)

DetailsButton = Button(text = "Add", width = 15, height = 3, bg = "white", fg = "black", command = add_details)
DetailsButton.place(x = 500, y = 700)

Listbox1 = Listbox(width = 40, height = 30)
Listbox1.place(x = 30, y  = 200)
