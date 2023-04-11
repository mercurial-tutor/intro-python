from interview.fizzbuzz import fizzbuzz

def test_fizzbuzz():
    # here are the fizzbuzz test cases
    assert fizzbuzz(3) == 'fizz'
    assert fizzbuzz(5) == 'buzz'
    assert fizzbuzz(9) == 'fizz'
    assert fizzbuzz(10) == 'buzz'
    assert fizzbuzz(15) == 'fizzbuzz'
