#This file is created by AKHIL JAIN

from turtle import Turtle
import random as r
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        self.goto(r.randint(-500,500),r.randint(-350,350))
