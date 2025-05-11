# Darion Poole
# 04/25/25
# P4LAB1a
# Use turtle and loops to draw initials

#Import the library
import turtle

# Create the turle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()

# Set turtle optinos
pen.pensize(5)
pen.pencolor("purple")
pen.shape("turtle")

#Code to draw the shapes
for side in range(4):
    pen.forward(100)
    pen.left(90)

#While loop that executes 3 times
sides = 3

while sides > 0:
    pen.forward(100)
    pen.left(120)
    sides = sides - 1
