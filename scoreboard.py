from turtle import Turtle
from os import path

FONT = ("Bold", 24, "italic")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-230, 250)
        self.color("white")
        self.check_highscore()
        self.write_highscore_text()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level : {self.level}", align="center", font=FONT)
        self.write(f"Highest Score : {str(self.highScore)}")

    def level_up(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def write_highscore_text(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 250)

    def check_highscore(self):
        file = open("HighscoreData.txt", "r")
        for line in file.readlines():
            self.highScore = int(line)

        file.close()

    def write_score(self):
        file = open("HighscoreData.txt", "w")
        file.write(str(self.level) + "\n")
        self.update()

        file.close()
