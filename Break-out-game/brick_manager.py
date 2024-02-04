from turtle import Turtle

class BrickManager:
    # Initialize the BrickManager class with an empty list of bricks, and the starting position of the first brick.
    def __init__(self):
        self.bricks = []
        self.x_pos = -300
        self.y_pos = -100

    # Create a row of bricks with a given color, number of bricks, x-coordinate, and y-coordinate.
    def create_row(self, color, num_bricks, x, y):
        # Define the size of each brick.
        brick_size = 45
        # Loop through the number of bricks and create a new Turtle object for each one.
        for brick in range(num_bricks):
            new_brick = Turtle('square')
            # Set the size and appearance of the brick.
            new_brick.shapesize(stretch_wid=4, stretch_len=1)
            new_brick.penup()
            new_brick.color(color)
            # Set the position of the brick based on its order in the row.
            new_brick.goto(x + brick*brick_size*2, y)
            new_brick.setheading(90)
            # Add the brick to the list of bricks.
            self.bricks.append(new_brick)

    # Remove a single brick from the list and hide it from view.
    def remove_brick(self, brick):
        brick.hideturtle()
        brick.clear()
        self.bricks.remove(brick)

    # Remove all bricks from the list and hide them from view.
    def remove_all(self):
        # Use a copy of the list to avoid modifying the list while looping through it.
        for brick in list(self.bricks):
            brick.hideturtle()
            brick.clear()
            self.bricks.remove(brick)
