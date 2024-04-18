from Animal import Animal

class Bird(Animal):
    def __init__(self, animal_type, animal_name, can_fly):
        super().__init__(animal_type, animal_name)
        self.__can_fly = can_fly

    def get_can_fly(self):
        return self.__can_fly
