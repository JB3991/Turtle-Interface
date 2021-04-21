# From the turtle module import Turtle and Screen class
from turtle import Turtle, Screen
import random

# Assign Turtle to timmy variable
timmy = Turtle()

# Change the shape of the object
timmy.shape("turtle")

# Change the Colour of the object
timmy.color("red")

# Assign Screen to screen Variable
screen = Screen()


# # Moving the Turtle
# timmy.forward(100)

# # Draw a Square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# # Draw a dash Line
# for _ in range(10):
#
#     #Size of the line.
#     timmy.pensize(5)
#     timmy.pendown()
#     timmy.forward(20)
#     timmy.penup()
#     timmy.forward(20)

# # Draw any sided shape
# number_sides = 5
# for _ in range(number_sides):
# Divide the amount of angles by 360 with give us the turn size
#     angle = 360 / number_sides
#     timmy.forward(100)
#     timmy.right(angle)

# Draw all the shapes in random Colours

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# Create a function so we can call this in our for loop.
def draw_shape(number_sides):
    for _ in range(number_sides):
        angle = 360 / number_sides
        timmy.forward(100)
        timmy.right(angle)

# Run for all shape sizes between 3 and 11. then stop
for shape_size_num in range(3, 11):
    timmy.color(random.choice(colours))
    draw_shape(shape_size_num)

# When you run code, Screen will appear until you click
screen.exitonclick()
