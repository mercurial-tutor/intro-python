"""a simple scratchpad provided for experimentation purposes
"""
def say_hello(name):
    print('hello from ' + name)

if __name__ == '__main__':
    # add code below ...
    # print('new dawn, new day')
    # this is a comment
    # print('hi ... my name is brandon')
    # say_hello('gabe the billionaire')
    # say_hello('arie the evil genius')
    groceries = ['tomatoes', 'eggs', 'strawberries', 'milk', 'soda', 'banana bread', 'ramen']
    # print(groceries[6])
    # animal = 'jaguar'
    # print(animal[0])
    # animal = ['j', 'a', 'g', 'u', 'a', 'r']
    # print(animal[0])
    for grocery in groceries:
        print(grocery)

    i = 0
    while i < len(groceries):
        print(groceries[i])
        i += 1

    example = 'abababababababab'
    print(example[::2])
