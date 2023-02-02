from turtle import Turtle
ALIGN = "center"
FONT = ("Ironwood", 22, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data_highscore.txt") as data:
            high_score = data.read()
            self.high_score = int(high_score)
        self.shape("circle")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score : {self.score}, High score: {self.high_score}", move=False, align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data_highscore.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.display_score()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write("GAME OVER", move=False, align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        
        
        
