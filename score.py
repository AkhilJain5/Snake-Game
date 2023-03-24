#This file is created by AKHIL JAIN

from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color('#00ff00')
        self.penup()
        self.goto(0,300)
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.write(f"Score:{self.score}",align="center",font=("Algerian",24,"normal"))
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=("Algerian",24,"normal"))
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()