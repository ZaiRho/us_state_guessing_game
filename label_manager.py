from turtle import Turtle


class LabelManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_label(self, coordinate, text):
        self.goto(coordinate)
        self.write(f"{text}", True, "center", ("courier", 10, "normal"))
