# Darion Poole
# 04/25/25
# P4LAB1b
# Use turtle and loops to draw initials

#Import the library
import turtle

# Create the turle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()

# Set turtle options
pen.pensize(8)
pen.pencolor("blue")
pen.shape("turtle")


for sides in range(3):
    pen.left(45)
    pen.forward(100)

while sides > 0:
    pen.left(135)
    pen.forward(235)
    sides = sides - 2

pen.penup()
pen.left(90)
pen.forward(150)
pen.pendown()

for sides in range(1):
    pen.left(90)
    pen.forward(235)
    pen.right(90)

sides = 3

while sides > 0:
    pen.forward(50)
    pen.right(90)
    sides = sides - 1
    


    
    
    





    
    

    
    



