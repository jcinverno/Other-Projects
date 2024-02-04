from turtle import Turtle


class Ball:

    def __init__(self):
        self.ball = Turtle()
        self.ball.penup()
        self.ball.shape("circle")
        self.ball.color("white")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.ball.xcor() + self.x_move
        new_y = self.ball.ycor() + self.y_move
        self.ball.goto(new_x, new_y)

    def bouncey(self):
        self.y_move *= -1

    def bouncex(self):
        self.x_move *= -1

    def beginning(self):
        self.ball.goto(0, -225)
        self.x_move *= -1

    def speed(self):
        self.x_move *= 1.1
        self.y_move *= 1.1

    def reset_speed(self):
        self.x_move = 10
        self.y_move = 10

    def stop(self):
        self.x_move = 0
        self.y_move = 0

