# filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
def even(some_list):
    return list(filter(lambda x: x % 2 == 0, some_list))


# return the square of each element. The list is: [1,2,3,4,5,6,7,8,9,10].
def calculate_square(some_list):
    return list(map(lambda x: x ** 2, some_list))


# make a list of elements that are the squares of the even numbers in [1,2,3,4,5,6,7,8,9,10].
def calculate_square_even(some_list):
    return even(calculate_square(some_list))


list1 = [1,2,3,4,5,6,7,8,9,10]
print(even(list1))
print(calculate_square(list1))
print(calculate_square_even(list1))


# find_numbers(min, max) that will find all numbers that are a multiple of 7 but not a multiple of 5.
def find_numbers(min, max):
    new_list = list(x for x in range(min, max+1))
    return list(filter(lambda x: x % 7 == 0 and x % 5 != 0, new_list))
# print(find_numbers(1,35))


# Given an integer n, write a program that generates a dictionary with entries from 1 to n.
# For each key i, the corresponding value should be i*i.
def generator(num):
    return {x: x ** 2 for x in range(1, num)}
# print(generator(10))


# Write a small script that will print numbers 1-10 in a way that if the number is even it prints the number,
# if the number is odd it print underscore _:
def print_even(num):
    filtered = list(filter(lambda x: x % 2 == 0, num))
    return ''.join('_' + str(x) for x in filtered)
# print(print_even(list1))
