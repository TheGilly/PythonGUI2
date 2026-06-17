from tkinter import *
import gtts
from tkinter import messagebox

def TextToSpeech():
    words = textentry.get("1.0", "end-1c")
    speech = gtts.gTTS(text = words, lang = "en")
    speech.save("output.mp3")
    messagebox.showinfo("Sucess", "MP£ file saved")
    

Screen = Tk()
Screen.configure(bg = "blue")
Screen.title("Google Text To Speech Converter")
Screen.geometry("800x600")

titlelabel = Label(text = "Text to Speech", width = 20, height = 3, bg = "pink", font = (20))
titlelabel.place(x = 100, y = 50)

textentry = Text(width = 50, height = 3, bg = "white")
textentry.place(x= 100, y = 170)

enterbutton = Button(width = 30, height = 3, bg = "yellow", text = "Convert to Speech", font = (20), command = TextToSpeech)
enterbutton.place(x = 100, y = 300)



