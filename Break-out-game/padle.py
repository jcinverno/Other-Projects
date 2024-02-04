from turtle import Turtle


class Paddles:

    def __init__(self, position):
        self.paddle = Turtle()
        self.paddle.penup()
        self.paddle.speed("fastest")
        self.paddle.color("white")
        self.paddle.shape("square")
        self.paddle.shapesize(10, 1)
        self.paddle.setheading(90)
        self.paddle.goto(position, -250)

    def left(self):
        coordinate_x = self.paddle.xcor() - 40
        coordinate_y = self.paddle.ycor()
        self.paddle.goto(coordinate_x, coordinate_y)

    def right(self):
        coordinate_x = self.paddle.xcor() + 40
        coordinate_y = self.paddle.ycor()
        self.paddle.goto(coordinate_x, coordinate_y)
