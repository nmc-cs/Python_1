# import os

# median function
def median(numbers):
    numbers = sorted(numbers)
    size = len(numbers)
    if size < 1:
        return None
    if size % 2 == 1:
        return numbers[size // 2]
    else:
        return sum(numbers[size // 2 - 1:size // 2 + 1]) / 2.0

# mode
def mode(l):
    d = {}
    for i in l:
        d.setdefault(i, 0)
        d[i] += 1

    max_count = max(d.values())
    modes = [key for key, count in d.items() if count == max_count]

    return modes if max_count > 1 else l


# main
if __name__ == "__main__":
    choice = 'y'
    while choice.lower() == 'y':
        # getting file name
        filename = input("Enter the filename: ")

        try:
            #used for debugging
            # # providing absolute path
            # filename = os.path.abspath(filename)

            # opening and reading from the file
            with open(filename, "r") as f:
                numbers = [int(num) for line in f for num in line.split()]

            # converting into integer numbers
            numbers = list(map(int, numbers))

            print("Filename: ", filename)
            print("Sum: ", sum(numbers))
            print("Count: ", len(numbers))
            print("Average: ", sum(numbers) / len(numbers))
            print("Maximum: ", max(numbers))
            print("Minimum: ", min(numbers))
            print("Range: ", max(numbers) - min(numbers))
            print("Median: ", median(numbers))
            print("Mode: ", mode(numbers))
        #exceptions to see if the file is being found druing debugging
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except ValueError:
            print("Error: File contains non-integer values.")

        choice = input("Do you want to read another file? y/n: ")
