import turtle
import os
import pandas as pd
from point import Point

screen = turtle.Screen()
screen.title("US States Game")
current_working_directory = os.getcwd()
path_to_files = "/usstates_game/day-25-us-states-game-start"
img = current_working_directory + path_to_files + "/blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)

df = pd.read_csv(f"{current_working_directory}{path_to_files}/50_states.csv")
list_of_states = df["state"].to_list()
correct_guesses = []
while len(correct_guesses) < 50:
    if len(correct_guesses) == 0:
        title = "Guess the States"
    else:
        title = f"{len(correct_guesses)}/50 States Guessed."
    answer_state = screen.textinput(title=title, prompt="What's another state's name? ")
    formated_answer_state = answer_state.title() # Format answer
    if formated_answer_state == "Exit":
        break
    if formated_answer_state in list_of_states:
        correct_guesses.append(formated_answer_state)
        x_cor = float(df[df["state"] == formated_answer_state]["x"])
        y_cor = float(df[df["state"] == formated_answer_state]["y"])
        pointy = Point()
        pointy.name_the_state(x_cor, y_cor, formated_answer_state)


missing_states = [item for item in list_of_states if item not in correct_guesses]
df = pd.DataFrame(missing_states)
df.to_csv("states_to_learn.csv")

