import turtle
import pandas as pd
from label_manager import LabelManager

screen = turtle.Screen()
label = LabelManager()

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pd.read_csv("50_states.csv")
data_x = data.x.to_list()
data_y = data.y.to_list()
coordinates = []

for i in range(len(data_x)):
    coordinates.append((data_x[i], data_y[i]))

state_list = data.state.to_list()

score = 0
guess = ""
game_over = False

screen.title(f"{score}/50 States Correct")


def evaluate_guess():
    global score
    if guess in state_list:
        x = state_list.index(guess)
        state_coordinate = coordinates[x]
        label.write_label(state_coordinate, guess)
        score += 1
    else:
        return


def guess_state():
    global guess
    guess = turtle.textinput(f"{score}/50 States Correct", "Name another US state").title()


def on_exit():
    turtle.done()


while not game_over:
    guess_state()
    evaluate_guess()

screen.exitonclick()
