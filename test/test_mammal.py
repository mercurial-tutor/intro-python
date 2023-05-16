from zoo.mammal import Mammal

def test_mammal():
    """a simple test suite for verifying our Mammal class implementation"""
    # first start by creating a mammal
    naked_mole_rat = Mammal("Morty", -1)

    assert naked_mole_rat.is_verterbrate
    assert naked_mole_rat.warm_blooded

    assert naked_mole_rat.eat("worms") == "Morty the Mammal ate the worms"
    assert naked_mole_rat.pet() == "you pet Morty the Mammal ... but it's completely bald!"

    # let's create a second mammal with different properties
    dog = Mammal("Lassie", 10)

    assert dog.is_verterbrate
    assert dog.warm_blooded

    assert dog.eat("treat") == "Lassie the Mammal ate the treat"
    assert dog.pet() == "you pet Lassie the Mammal ... wow, fluffy!"
