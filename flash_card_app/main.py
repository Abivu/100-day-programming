BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random
# ------------------------------------------FUNCTIONS----------------------------------------------------------#
try:
    df = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError or KeyError:
    df = pd.read_csv("./data/french_words.csv")
list_of_words = df.to_dict(orient="records")

current_card = {}


def new_word(*button_id):
    global flip_timer, current_card
    current_card = random.choice(list_of_words)
    try:
        window.after_cancel(flip_timer)
    except KeyError:
        pass
    new_word = current_card["French"]
    app.itemconfig(image, image= card_front)
    app.itemconfig(gen_word, text = new_word, fill="black")
    app.itemconfig(tile, text="French", fill="black")
    flip_timer = window.after(3000, flip_card)
        # remove the element from list_of_words
    
    if button_id[0] == 1:
        # Action when pressed wrong button
        print("You're pressing the button wrong")
    elif button_id[0] == 2:
        print("You're pressing the button right")

        list_of_words.remove(current_card)
        data = pd.DataFrame(list_of_words)
        data.to_csv("data/words_to_learn.csv")


def button_clicked(button_id):
    new_word(button_id)


def flip_card():
    en_mean = current_card["English"]
    card_back = PhotoImage(file="./images/card_back.png")
    app.itemconfig(image, image= card_back)
    app.itemconfig(tile, text = "English", fill= "white")
    app.itemconfig(gen_word, text = en_mean, fill="white")


# ------------------------------------------UI SET UP----------------------------------------------------------#
window = Tk()
window.title("Flashcard")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

app = Canvas(width=800, height=526)
card_front = PhotoImage(file="./images/card_front.png")
image = app.create_image(400, 263, image= card_front)
tile = app.create_text(400, 150, text="French/English FlashCard", font=("Ariel", 40, "italic"))
gen_word = app.create_text(400, 280, text="", font=("Ariel", 60, "bold"))
app.config(bg=BACKGROUND_COLOR, highlightthickness=0)
app.grid(column=1, row=1, columnspan=2)

flip_timer = window.after(3000, flip_card)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=lambda: button_clicked(1))
wrong_button.grid(column=1, row=2)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=lambda: button_clicked(2))
right_button.grid(column=2, row=2)


window.mainloop()

