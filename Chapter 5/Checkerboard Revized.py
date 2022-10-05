import turtle as tur
import my_graphics as graph

def checkerboard():
    #accepts no arguments
    #uses my graphics to draw a checkerboard
    #alternates between black and white
    
    #sets turtle speed to instant
    tur.speed(0)
    
    #assigns variables
    X_COR = -125
    X_ADD = 50
    
    Y_COR = -125
    Y_ADD = 50
    
    minimum = 1
    maximum = 5
    
    #outputs first column
    for num in range(1, 5+1):
        for num in range(minimum, maximum+1):
            if num%2 == 0:
                graph.square(X_COR, Y_COR, 50, "white")
            else:
                graph.square(X_COR, Y_COR, 50, "black")
            Y_COR += Y_ADD
        minimum += 5
        maximum += 5
        Y_ADD *= -1
        Y_COR += Y_ADD
        X_COR += X_ADD
    tur.done()