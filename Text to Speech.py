import tkinter as tk
from tkinter import *
import pyttsx3

engine=pyttsx3.init()

root=Tk()
root.title("Text to Speech")
root.geometry("500x200")
root.resizable(False,False)


def speaknow():
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop()

textv = StringVar()

obj=LabelFrame(root,text="Text to Speech",font=20,bd=1)
obj.pack(fill="both",expand="yes",padx=10,pady=10)

lbl=Label(obj,text="Text",font=30)
lbl.pack(side=tk.LEFT,padx=5)

ent=Entry(obj,textvariable=textv,font=30,width=25,bd=5)
ent.pack(side=tk.LEFT,padx=10)

btn=Button(obj,text="Speak",font=30,bg="black",fg="white",bd=2,command=speaknow)
btn.pack(side=tk.RIGHT,padx=3,pady=3)


root.mainloop()
