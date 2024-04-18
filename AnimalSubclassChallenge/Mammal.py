from Animal import Animal

class Mammal(Animal):
    def __init__(self, animal_type, animal_name, hair_color):
        super().__init__(animal_type, animal_name)
        self.__hair_color = hair_color

    def get_hair_color(self):
        return self.__hair_color
