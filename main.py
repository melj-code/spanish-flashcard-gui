from tkinter import *
import pandas
import random

current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/spanish_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_card)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(canvas_image, image=front_card_image)
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

def flip_card():
    global current_card
    canvas.itemconfig(canvas_image, image=back_card_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# data = pandas.read_csv("./data/spanish_words.csv")
# data.dropna(inplace=True)
# to_learn = data.to_dict(orient='records')

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Spanish Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# Images
wrong_image = PhotoImage(file="./images/wrong.png")
right_image = PhotoImage(file="./images/right.png")
# front_card_image = PhotoImage(file="./images/card_front.png")


canvas = Canvas(width=800, height=526)
front_card_image = PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=front_card_image)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# card_back = Label(image=back_card_image, highlightthickness=0)
# card_back.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)
wrong_button.config(bg=BACKGROUND_COLOR)

right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)
right_button.config(bg=BACKGROUND_COLOR)

known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# 1. After a delay of 3s (3000ms), the card should flip and display the English translation for the current word.
back_card_image = PhotoImage(file="./images/card_back.png")

next_card()

window.mainloop()
