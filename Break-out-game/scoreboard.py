from turtle import Turtle

# Set up constants for the scoreboard
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

with open("data.txt") as file:
    HIGH_SCORE = file.read()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(HIGH_SCORE)
        self.lives = '\u2764\uFE0F' + '\u2764\uFE0F' + '\u2764\uFE0F'
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")
        self.clear()
        self.write(f"Score: {self.score} Lives: {self.lives} ", align=ALIGNMENT, font=FONT)

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_scoreboard()
        self.goto(0, -150)
        self.write(f"GAME OVER\nHigh Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self, level):
        self.score += 2 ** level
        self.update_scoreboard()

    def decrease_lives(self, lives):
        if lives == 2:
            self.lives = '\u2764\uFE0F' + '\u2764\uFE0F'
        if lives == 1:
            self.lives = '\u2764\uFE0F'
        if lives == 0:
            self.lives = ''
        self.update_scoreboard()


