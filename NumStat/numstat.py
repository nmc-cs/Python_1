
def integerFile():
    try:
        fileName = input("Enter filename: ")
        with open(fileName) as f:
            data = f.readlines()

        data = [int(i.strip("\n")) for i in data]
        print("Sum:", sum(data))
        print("Count:", len(data))
        print("Average: {0:.2f}".format(sum(data)/len(data)))
        print("Maximum:", max(data))
        print("Minimum:", min(data))
        print("Range:", max(data)-min(data))
    except:
        print("Invalid file name.")

if __name__ == "__main__":
    while(True):
        integerFile()
        goAgain = input("Would you like to evaluate another file? (y/n): ")
        if(goAgain.lower() != 'y'):
            break
