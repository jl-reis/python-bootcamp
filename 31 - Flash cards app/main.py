from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
WORD_FONT = ("Ariel", 40, "bold")
LANG_FONT = ("Ariel", 30, "italic")

chosen_word = {}
# ------------------- Translator engine -------------------- #

words_df = pandas.read_csv("data/french_words.csv")
bag_of_words = words_df.to_dict(orient="records")

try:
    words_to_learn_df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words_df.to_csv("data/words_to_learn.csv", index=False)
    words_to_learn_df = pandas.read_csv("data/words_to_learn.csv")

words_to_learn = words_to_learn_df.to_dict(orient="records")


def know_word():
    """Remove a known words from the bag"""
    global chosen_word
    words_to_learn.remove(chosen_word)
    new_words_to_learn_df = pandas.DataFrame.from_dict(words_to_learn)
    new_words_to_learn_df.to_csv("data/words_to_learn.csv", index=False)
    new_word()


def new_word():
    """Choose a new words from the bag"""
    global chosen_word, turn_card
    window.after_cancel(turn_card)
    chosen_word = random.choice(bag_of_words)
    canvas.itemconfig(word, text=chosen_word["French"], fill="black")
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(card, image=flashcard_front_img)
    turn_card = window.after(3000, flash_card)


def flash_card():
    """Show the translation of the word"""
    global chosen_word
    canvas.itemconfig(word, text=chosen_word["English"], fill="white")
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(card, image=flashcard_back_img)


# ------------------------- GUI --------------------------- #
window = Tk()
window.title("Flashcards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# flashcard
flashcard_front_img = PhotoImage(file="images/card_front.png")
flashcard_back_img = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 263, image=flashcard_front_img)
# language title
title = canvas.create_text(400, 150, text="", font=LANG_FONT)
# word translated
word = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

# buttons
right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=know_word)
right_button.grid(column=1, row=1)
wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=new_word)
wrong_button.grid(column=0, row=1)

turn_card = window.after(3000, flash_card)
new_word()

window.mainloop()
