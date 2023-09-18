BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random
# ------------------------------------------FUNCTIONS----------------------------------------------------------#
df = pd.read_csv("./data/french_words.csv")
list_of_words = df.to_dict(orient="records")
current_card = {}


def new_word():
    global flip_timer, current_card
    current_card = random.choice(list_of_words)
    window.after_cancel(flip_timer)
    new_word = current_card["French"]
    app.itemconfig(image, image= card_front)
    app.itemconfig(gen_word, text = new_word, fill="black")
    app.itemconfig(tile, text="French", fill="black")
    flip_timer = window.after(3000, flip_card) # I don't get this part


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
tile = app.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
gen_word = app.create_text(400, 280, text="", font=("Ariel", 60, "bold"))
app.config(bg=BACKGROUND_COLOR, highlightthickness=0)
app.grid(column=1, row=1, columnspan=2)

flip_timer = window.after(3000, flip_card)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=new_word)
wrong_button.grid(column=1, row=2)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=new_word)
right_button.grid(column=2, row=2)

new_word()

window.mainloop()

