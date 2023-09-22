from tkinter import *
import pandas
import random
from tkinter import messagebox

# -------------------------------CONSTANTS---------------------------------#
BACKGROUND_COLOR = "#B1DDC6"
GREEN = "#9bdeac"
FONT_NAME = "Courier"
cards= {}
current_card = {}
try:
    data = pandas.read_csv("data/words-to-learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/eng-words.csv")
    cards = original_data.to_dict(orient="records")
else:
    cards = data.to_dict(orient="records")
# ---------------------------KNOWN WORDS-----------------------------------#
def known_word():
    print(cards)
    cards.remove(current_card)
    data = pandas.DataFrame(cards)
    data.to_csv("data/words-to-learn.csv", index=False)
    next_card()
# ---------------------------NEXT CARD--------------------------------------#
def next_card():
    try:
        global current_card, flip_timer, cards
        window.after_cancel(flip_timer)
        current_card = random.choice(cards)
        canvas.itemconfig(image, image=front_image)
        canvas.itemconfig(title, text="English", fill="black")
        canvas.itemconfig(word, text=current_card["English"], fill="black")
        flip_timer = window.after(3000, func=flip_card)
    except IndexError:
        messagebox.showinfo(title="Congratulations!", message="You've completed all words")
        flip_timer = window.after(3000, func=flip_card)
# ---------------------------RESET TIMER------------------------------------#

def flip_card():
    global current_card
    canvas.itemconfig(image, image=back_img)
    canvas.itemconfig(title, text="Arabic", fill="white")
    canvas.itemconfig(word, text=current_card["Arabic"], fill="white")

# ------------------------------------SETUP-------------------------------#

# Window setup
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Cards
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="images\card_front.png")
back_img = PhotoImage(file="images/card_back.png")
image = canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)

# Title and word setup
title = canvas.create_text(400, 150, text="English", font=(FONT_NAME, 30, "bold"))
word = canvas.create_text(400, 250, text=f"word", font=(FONT_NAME, 70, "bold"))

# Buttons Setup
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, command=known_word)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()# flash-cards
