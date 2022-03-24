import random
import turtle

numStars = int(input("How many stars would you like to draw?(1-50): "))
star = turtle.Turtle()
random_length = random.randrange(140,360, 30)

def initialStart():
    '''Starts up the program and asks for star input, Setting up window and bg color'''    
    window  = turtle.Screen()
    window.bgcolor("black")

def draw_star():
    '''Draws a star'''
    for i in range(5):
        star.forward(random_length)
        star.right(144)

def drawInput():
    '''for loop to draw stars based on the input by user'''
    for count in range(numStars):
        turtle.colormode(255)
        star.color(random.randint(0,255),
                random.randint(0,255),
                random.randint(0,255))
        star.begin_fill()
        draw_star()
        star.end_fill()
        star.penup()
        star.goto(random.randint(-500, 500), random.randint(-400, 400))
        star.pendown()
    star.hideturtle()

def main():
    initialStart()
    drawInput()

main()
turtle.done()