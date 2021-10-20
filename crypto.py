from tkinter import *
import cryptocode
import random

window=Tk()
window.title("CRYPTOCODE")
window.geometry("500x430")
var = IntVar()

def entryget_input(event):
    global res1
    input_mess=text.get("1.0", END)
    var.set(random.random)
    res1=input_mess
def entryget_output(event):
    global res2
    input_pw=text.get("1.0", END)
    var.set(random.random)
    res2=input_pw
def input():
    text.delete("1.0", END)
    label.config(text="input?")
    text.bind("<Return>", entryget_input)
    text.wait_variable(var)
    text.delete("1.0", END)
    label.config(text="PW?")
    text.bind("<Return>", entryget_output)
    text.wait_variable(var)
    text.delete("1.0", END)
    result=cryptocode.encrypt(res1, res2)
    text.insert('1.0', result)
def output():
    text.delete("1.0", END)
    label.config(text="input?")
    text.bind("<Return>", entryget_input)
    text.wait_variable(var)
    text.delete("1.0", END)
    label.config(text="PW?")
    text.bind("<Return>", entryget_output)
    text.wait_variable(var)
    text.delete("1.0", END)
    result=cryptocode.decrypt(res1, res2)
    if result==False:
        text.insert('1.0', "Something Wrong!")
    else:
        text.insert('1.0', result)

text=Text()
label=Label(text="Encryption or Decryption?")
button_input = Button(text="Encryption", width=33, height=5, bg="blue", fg="yellow", command=input)
button_output = Button(text="Decryption", width=33, height=5, bg="blue", fg="yellow", command=output)
button_input.place(x=12, y=20)
button_output.place(x=247, y=20)

label.pack()
text.place(y=110)
window.mainloop()


