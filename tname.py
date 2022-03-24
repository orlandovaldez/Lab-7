import turtle
import random

window = turtle.Screen()
window.bgcolor("Beige")
turtle.colormode(255)

def colorChange():
    '''Change the color of the text in turtle randomly'''
    turtle.color(random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255))

style = ('Arial', 200, 'normal')

turtle.setpos(-10,100)
colorChange()
turtle.write('FREE',font = style, align = 'center')
turtle.penup()
turtle.setpos(0,-100)
colorChange()
turtle.pendown()
turtle.write('BILLY',font = style, align = 'center')
turtle.setpos(55,-300)
colorChange()
turtle.write('WILLY',font = style, align = 'center')



turtle.done()