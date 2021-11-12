from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())

        self.update_score()
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0

    def update_score(self):
        self.write(f"Score {self.score} High_Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
