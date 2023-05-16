from interview.palindrome import is_palindrome

def test_palindrome():
    assert is_palindrome('civic')
    assert is_palindrome('tacocat')
    assert is_palindrome('racecar')
    assert not is_palindrome('gabe and arie are the best students')
    assert not is_palindrome('summer')
