import random
filename = 'randomnum.txt'
file = open(filename, 'w')
while(True):
    try:
        n = int(input("How many random numbers do you want?: "))
        if n <= 0:
            print("Invalid input... Only enter positive integers. Try again: ")
            continue
    except ValueError:
        print("Invalid input... Only enter numerical values. Try again: ")
    else:
        break
while(True):
    try:
        low = int(input("What is the lowest the random number should be?: "))
        if low <= 0:
            print("Invalid input... Only enter positive integers. Try again: ")
            continue
    except ValueError:
        print("Invalid input... ONly enter numerical values. Try again: ")
    else:
        break
while(True):
    try:
        high = int(input("What is the highest the random number should be?: "))
        if high <= 0:
            print("Invalid input... Only enter positive integers. Try again: ")
            continue
    except ValueError:
        print("Invalid input... Only enter numerical values. Try again: ")
    else:
        break
for i in range(n):
    n = random.randint(low, high)
    file.write(str(n) + '\n')
file.close()
print("The random numbers were written to...", filename)