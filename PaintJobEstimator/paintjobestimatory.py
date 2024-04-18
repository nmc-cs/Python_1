import math

def main():
    while True:
        while True:
            sqft = input('Enter the sqaure feet of wall you want to paint: ')
            sqft = float(sqft)
            if (sqft < 0) or (sqft == 0):
                print('Sqare feet must be positive')
                continue
            else:
                break

        while True:
            price = input('Enter the price of paint per gallon: ')
            price = float(price)
            if (price < 0) or (price == 0):
                print('Price must be positive')
                continue
            else:
                break

        gallons = sqft / 350 #calcs the amount of gallons by sq footage
        hours = gallons * 6 #calcs time based on amount of gallons
        gallons = math.ceil(gallons) #math.ceil rounds the gallons value up
        paintCost = price * gallons #calcs cost of paint
        paintCost = math.ceil(paintCost)
        labor = 62.25 * hours
        totalCost = paintCost + labor

        print("Gallons: %3d, Hours: %.3f, Paint Cost: $%.3f, Labor: $%.3f, Total Cost: $%.3f" % (gallons, hours, paintCost, labor, totalCost))


        retry = input(' Do you want to estimate again(y/n)? ')
        if retry.lower() == 'y':
            pass
        elif retry.lower() == 'n':
            break
        else:
            break

main()
    
