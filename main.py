#This file is created by AKHIL JAIN

from turtle import*
from snake import Snake
from food import Food
from score import Score
import time
#screen fitting
screen=Screen()
screen.setup(width = 1.0, height = 1.0)
screen.bgcolor('#3c79b8')
screen.title('My Snake Game')
screen.tracer(0)
#pen settings
pencolor('pink')
pensize(10)
#border settings
hideturtle()
speed(1000)
penup()
forward(510)
pendown()
left(90)
forward(350)
left(90)
forward(1020)
left(90)
forward(700)
left(90)
forward(1020)
left(90)
forward(350)
snake=Snake()
food=Food()
score=Score()
#key functions
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

game_is_on= True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if (snake.head.distance(food)<15):                 
        #when snake meet food
        food.refresh()
        snake.extend()
        score.increase_score()
    if (snake.head.xcor()>500 or snake.head.xcor()<-500 or snake.head.ycor()>350 or snake.head.ycor()<-350): 
        #when snake meets wall
        game_is_on=False
        score.game_over()
        
    for seg in snake.segment:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg)<10:
            game_is_on=False
            score.game_over() 
        #when snake meets its own body

screen.exitonclick()
