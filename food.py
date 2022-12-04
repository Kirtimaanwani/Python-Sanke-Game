import random
from turtle import Turtle


class Food(Turtle):
    # sub_class(super_class)

    def __init__(self):
        super().__init__()   # used inheritance here, Turtle as super class and Food as its subclass
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # since turtle default size is of 20 so we need
        # to decrease it to 10
        self.color("orange")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """
        drops food at random location of screen
        """
        x_random = random.randint(-280, 280)
        y_random = random.randint(-280, 280)
        self.goto(x=x_random, y=y_random)
