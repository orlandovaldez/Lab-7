from itertools import cycle
import random
from tkinter import colorchooser
import turtle

from pip import main

window = turtle.Screen()
window.bgcolor("Beige")

def colorChange(string):
    '''Change the color of the text in turtle randomly'''
    colorBank = ["Red","Blue","Green","Orange","Purple","Yellow"]
    color = cycle(colorBank)

    for i in string:
        turtle.color(next(color))
        style = ('Arial', 200, 'normal')
        turtle.write(i, move = True, font = style, align = 'left')


def freeWilly():
    '''Writes FREE BILLY WILL using turtle out to the screen
       while alternating colors'''
    turtle.penup()
    turtle.setpos(-350,120)
    colorChange("FREE")
    turtle.penup()
    turtle.setpos(-350,-100)
    colorChange("BILLY")
    turtle.penup()
    turtle.setpos(-335,-320)
    colorChange("WILLY")
    turtle.hideturtle()

def main():
    freeWilly()


main()
turtle.done()