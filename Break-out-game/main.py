# Import necessary modules
from turtle import Screen
from padle import Paddles
from brick_manager import BrickManager
from ball import Ball
from scoreboard import Scoreboard
import time

# Define colors, level, and lives
colors = ['red', 'red', 'orange', 'orange', 'green', 'green', 'blue', 'blue']
level = 0
lives = 3

# Initialize screen, paddle, bricks, ball, and score
screen = Screen()
paddle = Paddles(0)
bricks = BrickManager()
ball = Ball()
score = Scoreboard()

# Set screen properties
screen.bgcolor("black")
screen.setup(1000, 700)
screen.title("Breakout Game")
screen.tracer(0)

# Listen for keyboard input
screen.listen()
screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")

# Create bricks
for i in range(len(colors)):
    bricks.create_row(colors[i], 10, -400, 250 - i * 25)

# Start game loop
game_is_on = True
while game_is_on:

    # Add a short delay and update screen
    time.sleep(0.1)
    screen.update()

    # Move ball
    ball.move()

    # Bounce ball if it hits top of screen
    if ball.ball.ycor() > 280:
        ball.bouncey()

    # Bounce ball if it hits sides of screen
    if ball.ball.xcor() > 470 or ball.ball.xcor() < -470:
        ball.bouncex()

    # Bounce ball if it hits paddle
    if ball.ball.ycor() < -230 and ball.ball.distance(paddle.paddle) < 100:
        ball.bouncey()

    # Decrease lives and reset bricks if ball falls off bottom of screen
    if ball.ball.ycor() < -280:
        if lives == 1:
            score.game_over()
            ball.stop()
            bricks.remove_all()
            game_is_on = False
        else:
            lives -= 1
            score.decrease_lives(lives)
            bricks.remove_all()
            for i in range(len(colors)):
                bricks.create_row(colors[i], 10, -400, 250 - i * 25)
            ball.bouncey()
            ball.beginning()

    # Remove brick and increase score if ball hits brick
    for brick in bricks.bricks:
        if ball.ball.distance(brick) < 40:
            bricks.remove_brick(brick)
            ball.bouncey()
            score.increase_score(level)

    # Create new set of bricks if all bricks have been removed
    if len(bricks.bricks) == 0:
        for i in range(len(colors)):
            bricks.create_row(colors[i], 10, -400, 250 - i * 25)
        ball.speed()
        ball.beginning()
        level += 1

# Exit game on click
screen.exitonclick()
