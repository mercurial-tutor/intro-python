"""imports the fizzbuzz function from the fizzbuzz.py file"""
from interview.fizzbuzz import fizzbuzz

def test_fizzbuzz():
    """fizzbuzz test cases"""
    assert fizzbuzz(3) == 'fizz'
    assert fizzbuzz(5) == 'buzz'
    assert fizzbuzz(6) == 'fizz'
    assert fizzbuzz(9) == 'fizz'
    assert fizzbuzz(10) == 'buzz'
    assert fizzbuzz(12) == 'fizz'
    assert fizzbuzz(15) == 'fizzbuzz'
