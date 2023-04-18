'''
   CS5001
   Fall 2022
   Elif Tirkes 
   Homework 3: PositionService 
'''

import PositionService
#import package PositionService to help with coordinate grabbing 
import turtle

t = turtle.Turtle() #global turtle 
RADIUS = 80 #global radius


def circle_draw():
    '''
    Function -- circle_draw
        sets the position for the turtle given coordinates grabbed using the positionservice.get_position_x()
        and positionservice.get_position_y() functions 
        and draws a circle using the globally set radius value. 
    Draws a circle at grabbed coordinates x and y using Turtle t
    '''
    t.clear()
    t.penup()
    #clear the screen of the previous drawing
    t.setposition(PositionService.get_position_x(), PositionService.get_position_y())
    #go to the x and y position of the click measured by the get_position_x() and get_position_y() function
    t.pendown()
    t.pencolor("green")
    #set pencolor to green
    t.circle(RADIUS)
    t.penup()
    

def measure_and_check_circle(x,y):
    '''
    Function -- measure_and_check_circle 
        defines the boundaries of an existing circle within an approximate square area around
        the circle. uses these boundary coordinates to determine if the user's clicks are within
        or outside of the circle. If the user clicks within the circles' boundaries, the circle is
        erased. If the user clicks outside of boundaries, click is ignored. If a click happens
        after a circle is erased and the canvas is blank, a new circle is drawn at the clicked coordinates. 
    Parameters:
        x -- X coordinate grabbed from PositionService.get_position_x
        y --Y coordinate of click grabbed from PositionService.get_position_y
    Determines if turtle can draw a circle at click coordinates if criteria mentioned above are met,
    if they are, calls for circle_draw() to draw the circle at click coordinates 
    '''
    #get the boundaries of a circle within a "square" area around the circle
    x_left = int(PositionService.get_position_x() - RADIUS)
    x_right = int(PositionService.get_position_x() + RADIUS)
    y_bottom = int(PositionService.get_position_y())
    y_top = int(PositionService.get_position_y() + 2 * RADIUS)
    # 2 * Radius to measure the "square" area from bottom to top

    #if click is inside the circle, erase the circle
    if (x_left <= x <= x_right) and (y_bottom <= y <= y_top):
        PositionService.set_visible(True)
        t.clear()
        PositionService.set_visible(False)
        #sets circle as not visible if click happens within circle  
        
    elif PositionService.is_visible() == False:
        #if user clicked inside the circle and the circle is erased, there is no circle on canvas.
        #draw a new circle using circle_draw() at click coordinates 
        PositionService.set_visible(True)
        PositionService.set_position(x,y)
        circle_draw()
    else:
        return
        


def main():
    s = turtle.Screen()
    s.bgpic("shape_window.png")
    t.pencolor("green")

    s.onscreenclick(measure_and_check_circle)
    #when screen is clicked by user, prompts function measure_and_check_circle 
    
    #onscreenclick calls the function measure_and_check_circle with the two coordinates clicked on the screen
    PositionService.set_position(0,0) #set starting coordinates at 0,0 if there is no circle yet
    circle_draw() #draw first circle 


if __name__ == "__main__":
    main()
