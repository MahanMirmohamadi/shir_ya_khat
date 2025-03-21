# import
import random
import tkinter as tk
from PIL import Image , ImageTk
# ------------------------------------------------------------------------------------------------------------------------------------------------
# funcation
def myfunc():
    items = ["shir" , "khat"]
    text = inputtext.get()
    coin = random.choice(items)
    if text == coin and coin == "shir":
        lbl.config(image = shir)
        result.config(text = "your win")
    elif text == coin and coin == "khat":
        lbl.config(image = khat)
        result.config(text = "your win")
    elif text != coin and coin == "shir":
        lbl.config(image = shir)
        result.config(text = "you are lose")
    elif text != coin and coin == "khat":
        lbl.config(image = khat)
        result.config(text = "your lose")
# -----------------------------------------------------------------------------------------------------------------------------------------------
# label and images
window = tk.Tk()
window.geometry('500x500')
window.title("shir ya khat game")
welcomelabel = tk.Label(window , text = "welcome to game please choose from shir and khat" , font = ('Arial' , 13) , fg = 'RED')
inputtext = tk.Entry(window)
image = Image.open("F:\images\shir.jfif")
shir = ImageTk.PhotoImage(image)
img = Image.open("F:\images\khat.jfif")
khat = ImageTk.PhotoImage(img)
lbl = tk.Label(window)
result = tk.Label(window , text = "")
button = tk.Button(window , text = "check" , command = myfunc)
# -----------------------------------------------------------------------------------------------------------------------------------------------
# pack
welcomelabel.pack()
inputtext.pack()
button.pack()
lbl.pack()
result.pack()
# ---------------------------------------------------------------------------------------------------------------------------------------------------
# run
window.mainloop()