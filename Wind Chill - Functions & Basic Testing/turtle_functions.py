'''
   CS5001
   Fall 2022
   Elif Tirkes
   Homework 2: Programming #1- Align Draw (Turtle functions)

'''
import turtle

def draw_square(t, length):
    '''
    Function -- draw_square
        Draws a square using Turtle with an input length integer
    Parameters:
        t = Turtle
        length = integer, used to determine side length of square
    Returns a turtle drawing a square with the given length in sides
    '''
    t.pencolor("blue")
    t.fillcolor("blue")
    t.penup()
    #prevent turtle from drawing as it moves 
    t.setposition(( -length / 2 ), ( -length / 2 ))
    #sets the initial position of the turtle approximately in the middle of
    #the background based on length, to center the square in the middle 
    t.pendown()
    #begin drawing with turtle
    t.forward(length)  
    t.left(90)
    #turn turtle 90 degrees 
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    
def draw_circle(t, radius):
    '''
    Function -- draw_circle
        Draws a circle using Turtle with an input radius (integer)
    Parameters:
        t = Turtle
        radius = integer, used to determine the radius of the circle
    Returns a turtle drawing a circle with the given radius
    '''
    t.pencolor("pink")
    t.fillcolor("pink")
    t.penup()
    #hide turtle, stop drawing
    t.setposition(0,-radius)
    #locates the turtle approximately in the middle of the image
    #and approximately in the middle of the previously drawn square 
    t.pendown()
    #start drawing
    t.circle(radius)


def custom_square(t, x_square, y_square, length):
    '''
    Function -- custom_square
        Draws a square using Turtle with user-input X,Y coordinates
    Parameters:
        t = Turtle
        length = integer, used to determine the length of the square
        x_square = integer input value determining the X coordinate of turtle
        y_square = integer input value determining the Y coordinate of turtle 
    Returns a turtle drawing a square at user-given X,Y values 
    '''
    t.penup()
    t.setposition(x_square , y_square)
    #sets the position of the turtle at custom X,Y coordinates
    t.pencolor("blue")
    #determine pen fill color 
    t.fillcolor("blue")
    #determine shape fill color 
    t.begin_fill()
    #start filling in the shape when drawing
    t.pendown()
    t.forward(length)
    t.left(90)  
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.end_fill()
    #stop filling in the shape when drawing

def custom_circle(t,x_circle, y_circle, radius):
    '''
    Function -- custom_circle
        Draws a circle using Turtle with user-input X,Y coordinates
    Parameters:
        t = Turtle
        radius = integer, used to determine the radius of the circle
        x_circle = integer input value determining the X coordinate of turtle
        y_circle = integer input value determining the Y coordinate of turtle 
    Returns a turtle drawing a circle at user-given X,Y values 
    '''
    t.penup()
    t.setposition(x_circle, y_circle)
    #sets the position of the turtle to the custom X,Y coordinates 
    t.pencolor("pink")
    t.fillcolor("pink")
    t.begin_fill()
    #start filling in the shape when drawing
    t.pendown()
    t.circle(radius)
    #draw a circle with given radius
    t.end_fill()
    #stop filling in the shape when drawing 
