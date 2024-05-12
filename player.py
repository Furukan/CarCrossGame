from turtle import Turtle

STARTING_POSITION = (0, -260)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 250


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")

        self.penup()

        self.goto(STARTING_POSITION)
        self.setheading(90)

        self.color("white")

    def walk(self):
        self.forward(MOVE_DISTANCE)

    def paint_finish_line(self):
        self.finishLinePainter = Turtle()
        self.finishLinePainter.hideturtle()
        self.finishLinePainter.penup()
        self.finishLinePainter.goto(400, FINISH_LINE_Y)
        self.finishLinePainter.pendown()
        self.finishLinePainter.pensize(3)
        self.finishLinePainter.pencolor("yellow")
        self.finishLinePainter.goto(-400, FINISH_LINE_Y)

    def go_start(self):
        self.goto(STARTING_POSITION)

    def finish_check(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
