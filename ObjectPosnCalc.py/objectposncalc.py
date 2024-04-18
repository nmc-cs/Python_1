# Description: Write a Python 3 program that accepts user input from the keyboard for the
#              initial position, initial velocity, acceleration, and time that has passed and
#              outputs the final position based on an equation provided in the requirements.
# -----------------------------------------------------------------------------------------------------


def calcfinalpos():
    #gets the user inputs to calc finalpos
    x0 = float(input('Enter initial position: '))
    v0 = float(input('Enter initial velocity: '))
    a = float(input('Enter acceleration: '))  
    t = float(input('Enter time: '))  

    xf = x0 + (v0 * t) + (0.5 * a * t**2)
    print('The final position is: ',xf)

calcfinalpos()
    

