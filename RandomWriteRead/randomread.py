count = 0
try:
    print('List of random numbers in randomnum.txt:')
    with open('randomnum.txt') as file:
        for numbers in file:
            count = count + 1
            print(numbers, end = '')
    print('Random numbers count:', count)
except(FileNotFoundError):
    print('The file \'randomnum.txt\' was not found in the directory!')