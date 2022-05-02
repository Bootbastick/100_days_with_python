from tkinter import *
import pandas as pd
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"


# Flashcard mechanism
try:
    words = pd.read_csv("words_to_learn.csv")
    word_dict = words.to_dict(orient="list")
except FileNotFoundError:
    words = pd.read_csv("data/german_words.csv")
    word_dict = words.to_dict(orient="list")
finally:
    first_time = True

def print_word():
    global first_time
    canvas.itemconfig(language_canvas_text, text="German")
    canvas.itemconfig(card, image=card_front_image)
    word = random.choice(word_dict["German"])
    card_back_img = PhotoImage(file="images/card_back.png")

    canvas.itemconfig(word_canvas_text, text=word)
    window.update()
    window.after(3000)
    canvas.itemconfig(card, image=card_back_img)
    index = word_dict["German"].index(word)
    canvas.itemconfig(language_canvas_text, text="English")
    canvas.itemconfig(word_canvas_text, text=word_dict["English"][index])
    if not first_time:
        word_dict["German"].remove(word)
        word_dict["English"].remove(word_dict["English"][index])
        df = pd.DataFrame.from_dict(word_dict)
        df.to_csv("words_to_learn.csv", index=False)
    first_time = False

def word_unknown():
    canvas.itemconfig(language_canvas_text, text="German")
    canvas.itemconfig(card, image=card_front_image)
    word = random.choice(word_dict["German"])
    card_back_img = PhotoImage(file="images/card_back.png")

    canvas.itemconfig(word_canvas_text, text=word)
    window.update()
    window.after(3000)
    canvas.itemconfig(card, image=card_back_img)
    index = word_dict["German"].index(word)
    canvas.itemconfig(language_canvas_text, text="English")
    canvas.itemconfig(word_canvas_text, text=word_dict["English"][index])


# UI setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)
word_canvas_text = canvas.create_text(400, 263, text="To start\n press any button", font=("Ariel", 60, "bold"))
language_canvas_text = canvas.create_text(400, 150, text="German", font=("Ariel", 40, "italic"))

right_button_img = PhotoImage(file="images/right.png")
right = Button(image=right_button_img, highlightthickness=0, command=print_word)
right.grid(row=1, column=1)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_button_img, highlightthickness=0, command=word_unknown)
wrong.grid(row=1, column=0)


window.mainloop()
