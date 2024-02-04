from turtle import Screen
from padles import Padles
from ball import Ball
from scoreBoard import ScoreBoard
import time

screen = Screen()
Rpadle = Padles(350)
Lpadle = Padles(-350)
ball = Ball()
score = ScoreBoard()
game_is_on = True

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Game")
screen.tracer(0)

screen.listen()
screen.onkey(Rpadle.up, "Up")
screen.onkey(Rpadle.down, "Down")

screen.onkey(Lpadle.up, "w")
screen.onkey(Lpadle.down, "s")


while game_is_on:
    
    time.sleep(0.1)
    screen.update()
    ball.move()
    score.update()
    bc = ball.ball.xcor()

    if ball.ball.ycor() > 270 or ball.ball.ycor() < -270:
        
        ball.bouncey()
        ball.speed()
        
    if bc > 320 and ball.ball.distance(Rpadle.padle) < 40 or bc < -320 and ball.ball.distance(Lpadle.padle) < 40:  

        ball.bouncex()
        ball.speed()
        
    if  bc > 380:
        
        ball.reset_speed()
        ball.beginning()
        score.lscore()
        score.update()

    if bc < -380:
        
        ball.reset_speed()
        ball.beginning()
        score.rscore()
        score.update()


screen.exitonclick()
