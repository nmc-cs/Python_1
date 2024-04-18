
choice = 'y'
while choice == 'y':
    i = 1
    while i == 1:
        i = 0
        try:
            x0 = float(input('Enter initial position: '))
            v0 = float(input('Enter initial velocity: '))
            a = float(input('Enter acceleration: '))
            
            j = 1
            while j == 1:
                t = float(input("Enter time: "))
                if t > 0:
                    j = 0
                else:
                    print('Negative elapsed time error, try again')
                    j = 1
            break
        except ValueError:
            print("Wrong input... Start Over")
            i = 1
    
    xf = x0 + (v0 * t) + (0.5 * a * t**2)
    
    print("The final distance is " + str(xf))
    
    choice = input('Do you want to start over? : ')
