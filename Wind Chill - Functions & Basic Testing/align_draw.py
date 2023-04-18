'''
   CS5001
   Fall 2022
   Elif Tirkes
   Homework 2: Programming #1- Align Draw

'''

import turtle
from turtle_functions import draw_square
from turtle_functions import draw_circle
from turtle_functions import custom_square
from turtle_functions import custom_circle

LENGTH = 80
#chosen length for the drawn square based on prompt 
radius = LENGTH / 2
#radius of the drawn circle divided by two so it
#will fit into the drawn square


def main():
    t = turtle.Turtle()
    turtle.bgpic("shape_window.png")
    #inserts a custom background image
    
    draw_square(t, LENGTH)
    draw_circle(t, radius)
    t.clear()
    # clear the screen from the previous drawings 

    x_square = int(input("Please give a new X coordinate for the square "))
    #get custom x coordinate input for the square 
    y_square = int(input("Please give a new Y coordinate for the square "))
    #get custom y coordinate input for the square
    
    x_circle = int(input("Please give a new X coordinate for the circle "))
    #get custom x coordinate input for the circle 
    y_circle = int(input("Please give a new Y coordinate for the circle "))
    #get custom x coordinate input for the circle 

    custom_square(t,x_square, y_square, LENGTH)
    #call the custom_square function with the custom X,Y coordinates 
    #and with the previously used length
    
    custom_circle(t,x_circle, y_circle, radius)
    #call the custom_circle function with the custom X,Y coordinates 
    #and with the previously used radius

    

if __name__ == "__main__":
    main()
