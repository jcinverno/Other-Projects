# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 20:43:29 2022

@author: jcinv
"""

from tkinter import *
from PIL import Image, ImageDraw, ImageFont, ImageTk

URL1 = "image1.png"


def open_merge(raw, text, color):
        
    #merge images
    img1 = (Image.open(raw))
    width, height = img1.size
    newsize = (int(width/3), int(height/3))
    img1 = img1.resize(newsize)
    d = ImageDraw.Draw(img1)
    try:
        d.text((30,30), f"{text}", fill=color)
    except:
        d.text((30,30), f"{text}", fill='white')
    img1.show()
    img1.save(f'{text}.png')


def submit():
    
    url = entry.get()
    text = entry1.get()
    try:
        color = entry2.get()
    except:
        color = 'dark blue'

    open_merge(url, text, color)


# ---------------------- UI SETUP ------------------------ #
window = Tk()
window.title('Watermarking App')
window.geometry("550x500")
window.config(bg='white')
canvas = Canvas(width=600, height=500, bg='white', highlightthickness=0)

#image
img= (Image.open(URL1))
resized_image= img.resize((300,210), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
canvas.create_image(120,10, anchor=NW, image=new_image)


#text
canvas.create_text(270, 230, text="WATERMARKING APP", fill="dark blue", font=('Helvetica 25 bold'))

#entry
entry = Entry (width=50, fg='grey') 
entry.insert(0, "Path")
canvas.create_window(330, 300, window=entry)

entry1 = Entry (width=50, fg='grey') 
entry1.insert(0, "Your text")
canvas.create_window(330, 350, window=entry1)

entry2 = Entry (width=50, fg='grey') 
entry2.insert(0, "Color ")
canvas.create_window(330, 400, window=entry2)


#label
canvas.create_text(270, 230, text="WATERMARKING APP", fill="dark blue", font=('Helvetica 25 bold'))

canvas.create_text(100, 300, text="URL Image:", fill="dark blue", font=('Helvetica 12 bold'))

canvas.create_text(100, 350, text="Watermark text:", fill="dark blue", font=('Helvetica 12 bold'))

canvas.create_text(100, 400, text="Color:", fill="dark blue", font=('Helvetica 12 bold'))


#Button
go = Button(canvas, text= "Submit", font=('Helvetica 12 bold'), fg='white', bg='dark blue' , command=submit)
canvas.create_window(270, 450, window=go)

canvas.grid(column=0, row=0)
window.mainloop()
