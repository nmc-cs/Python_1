# imports hte Animal class from Animal.py
from Animal import Animal
#shows a welcome message in output
print("Welcome to the animal generator!")
print("This program creates Animal objects.\n")

# initializes an empty list so that we can store the animal obj
animal_list = []

# allows user to create multiple animal obj, loops
while True:
    animal_type = input("What type of animal would you like to create? ")
    animal_name = input("What is the animal's name? ")

    new_animal = Animal(animal_type, animal_name)
    animal_list.append(new_animal)

    print()
    choice = input("Would you like to add more animals (y/n)? ")
    print()
# user can decide to beak loop and not add animal objects
    if choice.lower() != "y":
        break
# if, checks if there are animals in the list before displaying them then displays the list of created animals with
# names, types and moods
if len(animal_list) > 0:
    print("Animal List:")
    for animal in animal_list:
        print(f"{animal.get_name()} the {animal.get_animal_type()} is {animal.check_mood()}")
