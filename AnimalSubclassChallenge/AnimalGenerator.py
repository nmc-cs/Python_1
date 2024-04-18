from Mammal import Mammal
from Bird import Bird

print("Welcome to the animal generator!")
print("This program creates Animal objects")

animal_list = []

while True:
    print("Would you like to create a mammal or bird?")
    print("1. Mammal")
    print("2. Bird")
    choice = int(input("Which would you like to create? "))

    if choice == 2:
        bird_type = input("What type of bird would you like to create? ")
        bird_name = input("What is the bird's name? ")
        can_fly = input("Can the bird fly? ")
        animal_list.append(Bird(bird_type, bird_name, can_fly))
    elif choice == 1:
        mammal_type = input("What type of mammal would you like to create? ")
        mammal_name = input("What is the mammal's name? ")
        hair_color = input("What color is the mammal's hair? ")
        animal_list.append(Mammal(mammal_type, mammal_name, hair_color))
    print()
    choice = input("Would you like to add more animals (y/n)? ")
    print()
    if choice == "n":
        break

if len(animal_list):
    print("Animal List")
    for animal in animal_list:
        print(animal.get_name() + " the " + animal.get_animal_type() + " is " + animal.check_mood())
