from zoo.animal import Animal
from zoo.mammal import Mammal

def test_mammals():
    """a simple test suite for verifying our Mammal class implementation"""
    # first start by creating a mammal
    naked_mole_rat = Mammal("Morty", -1)

    # check the properties, they should both be True
    assert naked_mole_rat.is_verterbrate
    assert naked_mole_rat.warm_blooded

    # try out the functions
    assert naked_mole_rat.eat("worms") == "Morty the Mammal ate the worms"
    assert naked_mole_rat.pet() == "you pet Morty the Mammal ... but it's completely bald!"

    # notice that the naked mole is rat is an instance of BOTH Mammal and Animal!
    assert isinstance(naked_mole_rat, Mammal)
    assert isinstance(naked_mole_rat, Animal)

    # let's create a second mammal with different properties
    dog = Mammal("Lassie", 10)

    assert dog.is_verterbrate
    assert dog.warm_blooded

    assert dog.eat("treat") == "Lassie the Mammal ate the treat"
    assert dog.pet() == "you pet Lassie the Mammal ... wow, fluffy!"

    assert isinstance(dog, Mammal)
    assert isinstance(dog, Animal)
