class Animal:
    """this is our animal interface, it defines common properties of all animals"""
    def __init__(self, name: str, is_verterbrate: bool, warm_blooded: bool):
        # all animals have names
        self.name = name
        # all animals are either verterbrates or inverterbrates
        self.is_verterbrate = is_verterbrate
        # all animals are either warm or cold-blooded
        self.warm_blooded = warm_blooded

    def eat(self, food: str):
        """
        all animals eat
        :param food: the item to be eaten by a particular animal
        """
        return f"{self.name} the {self.__class__.__name__} ate the {food}"
