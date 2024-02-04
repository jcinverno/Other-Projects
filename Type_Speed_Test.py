"""Using Tkinter and what you have learnt about building GUI
applications with Python, build a desktop app that assesses
your typing speed. Give the user some sample text and detect
how many words they can type per minute."""

"""API: https://api-ninjas.com/examples/basic-web-app"""
# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
import requests
from datetime import datetime

# ---------------------------- CONSTANTS ------------------------------- #

ORANGE_LIGHT = "#FED8B1"
ORANGE_STRONG = "#F58025"

category = 'learning'
API_KEY = 'WVLQMA1Ugt816ZxHTOIbdQ==r7a7kFHJfxhll6o4'
api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)

n = 0
delta = 0


# ---------------------------- DIVIDE SENTENCE ------------------------------- #
def divide(texto):
    chunks = []
    current_chunk = ""
    words = texto.split()
    for word in words:
        if len(current_chunk) + len(word) <= 80:
            current_chunk += word + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = word + " "
    chunks.append(current_chunk.strip())
    return "\n".join(chunks)


# ---------------------------- GET FIRST SENTENCE ------------------------------- #
response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
r1 = requests.get(api_url, headers={'X-Api-Key': API_KEY}).json()
r2 = requests.get(api_url, headers={'X-Api-Key': API_KEY}).json()

texto = f'{r1[0]["quote"]} {r2[0]["quote"]}'
novo = divide(texto)

if response.status_code == requests.codes.ok:
    print(texto)
else:
    print("Error:", response.status_code, response.text)


# ---------------------------- SUBMIT SENTENCE ------------------------------- #
def submit():
    global delta

    letters = len(texto)
    Gross_WPM = round((letters / 5) / (delta / 60), 2)
    top = Toplevel(window)
    top.geometry("200x150")
    top.config(pady=50, bg=ORANGE_LIGHT)
    top.title("WPM")
    wpm = Label(top, text=f"WPM: {Gross_WPM}", font=("Arial", 15), bg=ORANGE_LIGHT)
    wpm.pack()


# ---------------------------- GET LETTER ------------------------------- #
def update_text(event):
    global start_time, delta, n
    key = event.char

    # start time
    if texto[0] == key and n == 0:
        start_time = datetime.now()
        print('Start time:', start_time)
        n += 1

    # finish
    try:
        if texto[n] == key and n != 0:
            n += 1

    except IndexError:
        end_time = datetime.now()
        print('End time:', end_time)
        delta = end_time - start_time
        delta = delta.total_seconds()
        print(f"Time difference is {delta} seconds")
        submit()


# ---------------------------- RESET SENTENCE ------------------------------- #
def create_sentence():
    global texto, novo, n
    response1 = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    r11 = requests.get(api_url, headers={'X-Api-Key': API_KEY}).json()
    r21 = requests.get(api_url, headers={'X-Api-Key': API_KEY}).json()

    texto = f'{r11[0]["quote"]} {r21[0]["quote"]}'
    novo = divide(texto)

    if response1.status_code == requests.codes.ok:
        print(text)
        label.config(text=novo)
        n = 0
        cancel()
    else:
        print("Error:", response1.status_code, response1.text)


# ---------------------------- CANCEL ------------------------------- #
def cancel():
    global n
    text.delete(1.0, 'end')
    n = 0


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Typing Speed")
window.config(width=400, height=400)
window.config(padx=10, pady=50, bg=ORANGE_LIGHT)

label = Label(text=novo, font=("Arial", 15), bg=ORANGE_LIGHT)
label.grid(row=0, column=1, columnspan=4, padx=20, pady=20)

text = Text(height=7, width=60, font=("Arial", 15))
text.bind("<Key>", lambda event: update_text(event))
text.grid(row=1, column=1, columnspan=4, padx=20, pady=10)

button = Button(text="Cancel", command=cancel, width=20, font=("Arial", 15), bg=ORANGE_STRONG)
button.grid(row=2, column=2, pady=10)

button1 = Button(text="Reset", command=create_sentence, width=20, font=("Arial", 15), bg=ORANGE_STRONG)
button1.grid(row=2, column=3, pady=10)

window.mainloop()
