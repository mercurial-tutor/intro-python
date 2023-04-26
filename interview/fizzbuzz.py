def fizzbuzz(number: int) -> str:
    """fizzbuzz is a function which takes a number and returns ...
        - 'fizz' if the number is a multiple of 3
        - 'buzz' if the number is a multiple of 5
        - 'fizzbuzz' if the number is a multiple of 3 and 5

    :param number: the input integer provided by the user.
    :type number: int
    :returns: a string with some combination of 'fizz' and 'buzz' 
    :rtype: str
    """
    # TODO implement our fizzbuzz function ...
    answer = ''
    if number % 3 == 0:
        answer += 'fizz'
    if number % 5 == 0:
        answer += 'buzz'
    return answer
