# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 13:29:05 2021

@author: jcinv
"""

from turtle import Turtle


class ScoreBoard:
    
    def __init__(self):
        
        self.score = Turtle()
        self.score.color("white")
        self.score.penup()
        self.score.hideturtle()
        self.l_score = 0
        self.r_score = 0
       
        
    def lscore(self):
      
        self.l_score += 1
        
    def rscore(self):
        
        self.r_score += 1
        
    def update(self):
        
        self.score.clear()
        self.score.goto(-100,200)
        self.score.write(self.l_score, True, align="center", font=("Courier", 80, "normal"))
        self.score.goto(100, 200)
        self.score.write(self.r_score, True, align="center", font=("Courier", 80, "normal"))
        