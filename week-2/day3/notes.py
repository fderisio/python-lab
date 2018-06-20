# lambda functions are anonymous functions
# print(args)  # prints a tuple
# print(kwargs)
# print(list(args))  # prints a list
list1 = [1,2,3,4,5,6,7,8,9,10]
new_list = [x * 2 for x in list1]  # shorter for loop
new_dict = {x: x ** 2 for x in list1}  # list comprehension
######


def func_decorator(some_function):  # function decorator is a function inside another function
    print('Hi!, what\'s our name?')

    def wrapper(name):
        some_function(name)
    return wrapper


@func_decorator
def say_my_name(name):
    print(f'Hello {name}')


print(say_my_name('Hanna'))
#######


#some code here  # noqa (makes flake8 not to recognise the error)










