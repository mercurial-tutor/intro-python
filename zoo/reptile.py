from zoo.animal import Animal

class Reptile(Animal):
    """reptilia is a large subclass of animal"""
    def __init__(self, name: str, warm_blooded: bool, scale_level: int):
        # all reptiles are verterbrates ... but are all reptiles cold-blooded?
        super(Reptile, self).__init__(name, True, warm_blooded)
        # all reptiles have scales
        self.scale_level = scale_level

    def pet(self):
        """the pet function takes no arguments and produces different results based on scale level"""
        if self.scale_level <= 0:
            return f"you pet {self.name} the {self.__class__.__name__} ... it feels slimy, ew!"
        if self.scale_level > 0 and self.scale_level < 10:
            return f"you pet {self.name} the {self.__class__.__name__} ... so smooth."
        if self.scale_level >= 10:
            return f"you pet {self.name} the {self.__class__.__name__} ... wow, it's armored to the teeth!"