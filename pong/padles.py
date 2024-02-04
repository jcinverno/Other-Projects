from turtle import Turtle

class Padles:
    
    def __init__(self, position):
        
        self.padle = Turtle()
        self.padle.penup()
        self.padle.speed("fastest")
        self.padle.color("white")
        self.padle.shape("square")
        self.padle.shapesize(5, 1)
        self.padle.goto(position, 0)
    
    
    def up (self):
        
        coordenada_x = self.padle.xcor()
        coordenada_y = self.padle.ycor() + 40
        self.padle.goto(coordenada_x, coordenada_y)
       
        
    def down (self):
        
        coordenada_x = self.padle.xcor()
        coordenada_y = self.padle.ycor() - 20
        self.padle.goto(coordenada_x, coordenada_y)
        
        
        