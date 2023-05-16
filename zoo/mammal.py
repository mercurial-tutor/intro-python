from zoo.animal import Animal

class Mammal(Animal):
    """mammalia is a large subclass of animal"""
    def __init__(self, name: str, hair_level: int):
        # all mammals are warm-blooded verterbrates, so we can pass both arguments as True
        super(Mammal, self).__init__(name, True, True)
        # all mammals have hair, our "hair level" integer determines how fluffy each mammal is
        self.hair_level = hair_level

    def pet(self):
        """the pet function takes no arguments and produces different results based on hair level"""
        if self.hair_level <= 0:
            return f"you pet {self.name} the {self.__class__.__name__} ... but it's completely bald!"
        if self.hair_level > 0 and self.hair_level < 10:
            return f"you pet {self.name} the {self.__class__.__name__} ... how pleasant."
        if self.hair_level >= 10:
            return f"you pet {self.name} the {self.__class__.__name__} ... wow, fluffy!"
