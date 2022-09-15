import turtle as tur

def square(x, y, width, color):
    #accepts x and y as a start position
    #accepts a width for length of each side
    #accepts color for color of square
    #prints square using arguments
    
    tur.penup() #Raise the pen
    tur.goto(x, y) #Move to (x,y)
    tur.fillcolor(color) #Set the fill color
    tur.pendown() #Lower the pen
    tur.begin_fill() #Start filling
    for count in range(4): #Draw a square
        tur.forward(width)
        tur.left(90)
    tur.end_fill() #End filling
    
def circle(x, y, radius, color):
    #accepts x and y for start point
    #accepts a radius for size of circle
    #accepts color for color of circle
    #draws a circle using arguments
    
    tur.penup() #Raise the pen
    tur.goto(x, y - radius) #Move to (x,y)
    tur.fillcolor(color) #Set the fill color
    tur.pendown() #lower the pen
    tur.begin_fill() #start filling
    tur.circle(radius) #draws the circle
    tur.end_fill() #stops filling

def line(startX, startY, endX, endY, color):
    #accepts a start x and y for start point
    #accepts a end x and y for end point
    #accepts color for color of line
    
    tur.penup() #Raise the pen
    tur.goto(startX, startY) #Move to the starting point
    tur.pendown() #Lower the pen
    tur.pencolor(color) #Set the pen color
    tur.goto(endX, endY) #Draw a line
    










































