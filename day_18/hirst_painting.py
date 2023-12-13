import turtle as t
from turtle import Turtle, Screen
from random import choice, randint


# screen
screen = Screen()
screen.setup(width=700, height=800, startx=0, starty=0)
t.colormode(255)

# the turtle object/stats
turters = Turtle()
turters.shape("turtle")
turters.speed(6)
turters.pensize(10)

# Hirst color
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]


for _ in range(50):
    turters.penup()
    turters.forward(50)  # Move to the desired position without drawing
    turters.pendown()  # Put the pen down


# exit
Screen().exitonclick()
