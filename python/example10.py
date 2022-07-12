'''
# def name_of_function():
def name_of_function(name):
    """
    Docstring explains function.
    """
    # print('Hello')
    print(f'Hello {name}')


# name_of_function()
name_of_function('Andrew')
'''


'''
def add_function(num1, num2):
    return num1 + num2


result = add_function(1, 2)
print(result)
'''


'''
def say_hello():
    print('Hello!')
    print('another hello!')


say_hello()
say_hello()
'''


'''
def say_hello(first_name, last_name):
    return f'Hello {first_name} {last_name}'


# my_var = say_hello('esmai', 'baker')
my_var = say_hello(first_name='esmai', last_name='baker')

print(my_var)
'''


'''
def checker(num):
    if num > 100:
        return 'greater than 100'
    else:
        return 'not greater than 100'


print(checker(90))
print(checker(900))
'''


my_list = [1, 2, 5, 3, 1, 6, 7, 2, 8, 9, 10, 2, 1]


def checker(list_to_check):
    for num in list_to_check:
        if num == 10:
            return True

    return False


print(checker(my_list))
