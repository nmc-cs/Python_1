from random import randint

class Animal:
    def __init__(self, animal_type, animal_name):
        self.__animal_type = animal_type
        self.__name = animal_name
        r = randint(1, 3)
        if r == 1:
            self.__mood = "happy"
        elif r == 2:
            self.__mood = "hungry"
        else:
            self.__mood = "sleepy"

    def get_animal_type(self):
        return self.__animal_type

    def get_name(self):
        return self.__name

    def check_mood(self):
        return self.__mood
