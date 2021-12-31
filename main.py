import turtle
from us_state_name import StateName
from scoreboard import Scoreboard
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
turtle.addshape(image)

state_names = StateName()
states_scoreboard = Scoreboard()
turtle.shape(image)

state_dataset = pd.read_csv("50_states.csv")
state_list = state_dataset["state"].to_list()

states_guessed = 0
while states_guessed < len(state_list):
    answer_prompt = turtle.textinput(title = "Guess the state", prompt = "What is another state?")
    for state in state_list:
        if state.casefold() == answer_prompt.casefold():
            states_guessed += 1
            states_scoreboard.increment_score()
            state_row = state_dataset[state_dataset["state"] == state]
            x_cor = state_row["x"]
            y_cor = state_row["y"]
            state_names.set_name(state, x_cor, y_cor)
screen.exitonclick()