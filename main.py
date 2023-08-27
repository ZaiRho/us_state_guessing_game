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
# print(coordinates)
state_list = data.state.to_list()
state_to_guess = data.state.to_list()
guessed_state = []

score = 0
guess = ""
game_over = False

screen.title(f"US State Guessing Game")


def evaluate_guess():
    global score
    global game_over
    if guess == "Exit":
        game_over = True
    if guess in state_to_guess:
        x = state_list.index(guess)
        state_coordinate = coordinates[x]
        label.write_label(state_coordinate, guess)
        score += 1
        state_to_guess.remove(guess)
        guessed_state.append(guess)
    else:
        return


def guess_state():
    global guess
    guess = turtle.textinput(f"{score}/50 States Correct", "Name another US state").title()


def on_exit():
    turtle.done()


while not game_over:
    if score == 50:
        game_over = True
    guess_state()
    evaluate_guess()


state_remaining =[state for state in state_list if state not in guessed_state]
datum = pd.DataFrame(state_remaining)

datum.to_csv("state_to_review.csv")
