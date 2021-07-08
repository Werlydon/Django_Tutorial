# NAME

import turtle
import time
import random

turtle.delay(0.1)
score = 0
high_score = 0



# Creating a window screen
screen = turtle.Screen()
screen.title("SnakeGameplay")
screen.bgcolor("#FFD700")
screen.setup(width=475, height=600) 
#TODO: modify this, and use the input function to ask the user what size they want. 
# save those values and set it to the size of the window
screen.tracer(0)


head = turtle.Turtle()
head.shape("classic")
head.color("#C0C0C0")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# food in the game
food = turtle.Turtle()
colors = random.choice(['brown', 'red', 'green'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(32, 67) 


pen = turtle.Turtle()
pen.speed(0)
pen.shape()
pen.color()
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
#TODO write score



# assigning key directions
# TODO: key directions for going up and down
"""
def goleft():
	if head.direction != "right":
		head.direction = "left"


def goright():
	if head.direction != "left":
		head.direction = "right"


def move():
	if head.direction == "up":
		y = head.ycor()
        # TODO: what do we do after getting the coordinate? what does it mean to go up?
	if head.direction == "doscreen":
        # TODO: get coordinate and move down
	if head.direction == "left":
		        # TODO: get coordinate and move left

	if head.direction == "right":
	        # TODO: get coordinate and move right



		
screen.listen()

#TODO: call the functions on key press. example below, make sure you go left right and down.
screen.onkeypress(goup, "w")

segments = []



# Main Gameplay
while True:
    #TODO: make the code for the main game iteration, and make sure you call your functions. have the snake move random
	"""
screen.mainloop()