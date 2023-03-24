#This file is created by AKHIL JAIN

from turtle import Turtle
START_POSITION=[(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]
    def create_snake(self):
        for pos in START_POSITION:
            self.add_snake_body(pos)
    def add_snake_body(self,pos):
        new_segment=Turtle("circle")
        new_segment.penup()
        new_segment.color('black','#ff1a1a')
        new_segment.goto(pos)
        self.segment.append(new_segment)
    def extend(self):
        self.add_snake_body(self.segment[-1].position())
    def move(self):
        for seg in range(len(self.segment)-1,0,-1):
            new_x=self.segment[seg-1].xcor()
            new_y=self.segment[seg-1].ycor()
            self.segment[seg].goto(new_x,new_y)
        self.head.forward(20)
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)