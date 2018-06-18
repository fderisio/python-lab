import re

# def is_string(text):
#     if type(text) == str:
#         return True
#     else:
#         return False
#
# print(is_string('hello'))  # True
# print(is_string(['hello']))                  # False
# print(is_string('this is a long sentence'))  # True
# print(is_string({'a': 2}))                   # False
# print("-------------------")


def is_only_string(param):
    if type(param) == str:
        return param.isdigit() is not True or " " in param
    if type(param) == list:
        return list(map(lambda x: str(x).isdigit() is not True or " " in str(x), param))
    if type(param) == dict:
        return param.keys()
print(is_only_string('11'))                       # False
print(is_only_string('hello'))
print(is_only_string(['hello', 2]))               # ? Please handle this case!! Should return False
print(is_only_string('this is a long sentence'))  # False
print(is_only_string({'a': 2}))                   # ? Please handle this case!! Should return False

#
# def is_alphanumeric(param):
#     if type(param) == str:
#         return param.isdigit() is not True
#     if type(param) == list:
#         return re.match('/^ *[0-9][0-9 ]*$/', param)
#     if type(param) == dict:
#         return param.keys()
#
# print(is_alphanumeric('11'))                       # True
# print(is_alphanumeric(['hello']))                  # False
# print(is_alphanumeric('this is a long sentence'))  # False
# print(is_alphanumeric({'a': 2}))                   # False
# print(is_alphanumeric("this is string....!!!"))    # False


def is_array_or_tuple(param):
    return type(param) == list or type(param) == tuple

# print(is_array_or_tuple('hello'))      # False
# print(is_array_or_tuple(['hello']))    # True
# print(is_array_or_tuple([2, {}, 10]))  # True
# print(is_array_or_tuple({'a': 2}))     # False
# print(is_array_or_tuple((1, 2)))       # True
# print(is_array_or_tuple(set()))        # False


def are_same_type(param):
    comparison = type(param[0])
    for i in range(1, len(param)):
        if type(param[i]) != comparison:
            return False
    return True


# print(are_same_type(['hello', 'world', 'long sentence']))  # True
# print(are_same_type([1, 2, 9, 10]))                        # True
# print(are_same_type([['hello'], 'hello', ['bye']]))        # False
# print(are_same_type([['hello'], [1, 2, 3], [{'a': 2}]]))   # True
# print(are_same_type([['hello'], set('hello')]))            # False

from collections import OrderedDict
def intersection(str1, str2):
    return "".join(sorted(OrderedDict.fromkeys(str1 + str2)))

# a = 'xyaabbbccccdefww'
# b = 'xxxxyyyyabklmopq'
# x = 'abcdefghijklmnopqrstuvwxyz'
# print(intersection(a, b))  # abcdefklmopqwxy
# print(intersection(a, x))  # abcdefghijklmnopqrstuvwxyz


def convert(num):
    return sorted([int(x) for x in str(num)], reverse=True)


# print(convert(429563))  # [9, 6, 5, 4, 3, 2]
# print(convert(324))     # [4, 3, 2]


def count_repetition(names_array):
    result = {}
    for name in names_array:
        if result.get(name):
            result[name] += 1
        else:
            result[name] = 1
    return result

# names = ['kerouac', 'fante', 'fante', 'buk', 'hemingway', 'hornby', 'kerouac', 'buk', 'fante']
# print(count_repetition(names))
# {'kerouac': 2, 'fante': 3, 'buk': 2, 'hemingway': 1, 'hornby': 1}


def is_caught(str1):
    array1 = list(str1)
    for index, val in enumerate(array1):
        if val == "C" and array1[index+2] == "m" or \
                val == "C" and array1[index+3] == "m":
            return True
    return False

# print(is_caught('C.....m'))   # False
# print(is_caught('C..m'))      # True
# print(is_caught('..C..m'))    # True
# print(is_caught('...C...m'))  # False
# print(is_caught('C.m'))       # True


def split_the_bill(people):
    total_bill = 0
    for value in people.values():
        total_bill += value
    result = {}
    for key, value in people.items():
        result[key] = (total_bill / 3) - value
    return result

# group = {
#     'Amy': 20,
#     'Bill': 15,
#     'Chris': 10
# }
# print(split_the_bill(group))  # { 'Amy': -5, 'Bill': 0, 'Chris': 5 }


def exp_recursive(num1, num2):
    return num1 ** num2
# print(exp_recursive(5, 3))  # 125
# print(exp_recursive(2, 4))  # 16
# print(exp_recursive(5, 1))  # 5
# print(exp_recursive(6, 0))  # 1

def zero_sum(some_array):
    result = []
    for i, i_value in enumerate(some_array):
        for j, j_value in enumerate(some_array):
            if i_value + j_value == 0:
                result.append([i, j])
    return result
# print(zero_sum([1, 5, 0, -5, 3, -1]))  # [[0, 5], [1, 3], [2, 2]]
# print(zero_sum([1, -1]))               # [[0, 1]]
# print(zero_sum([0, 4, 3, 5]))          # [[0, 0]]


def letter_counter(string):
    count_upper = sum(1 for c in string if c.isupper())
    count_lower = sum(1 for c in string if c.islower())
    return "UPPER CASE: ", count_upper, "lower case:", count_lower
# print(letter_counter("Hello World!"))
# UPPER CASE 1
# LOWER CASE 9


def new_dict(array):
    result = {}
    for i in array:
        result[i] = ""
    return result
print(new_dict([1, 2, 3, 4, 5])) # {1: {2: {3: {4: {5: {}}}}}}

def bank_account():
    balance = 0
    option = 0
    while option == 0:
        option = input("Would you like to deposit, withdraw or see the balance? (d/w/b)")
        while option is not "d" or option is not "w" or option is not "b":
            option = input("Please choose one of these options: deposit, withdraw or see the balance? (d/w/b)")
        if option == "d":
            deposit = float(input("Insert amount to deposit: "))
            balance += deposit
            option = 0
        if option == "w":
            withdraw = float(input("Insert amount to withdraw: "))
            balance -= withdraw
            option = 0
    return "Bank Account - Balance:", balance
# print(bank_account())

import random
def nt_dictionary(num):
    result = {}
    for i in range(0, num):
        random_num = random.randint(1,1000)
        result[random_num] = random_num * random_num
    return result
# print(nt_dictionary(20))
# print('Length', len(nt_dictionary(20)))


import itertools
def permute(array):
    return list([list(e) for e in itertools.permutations(array)])
print(permute([1, 2, 3])) # [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]


def create_dictionary():
    numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
               10: "ten", 11: "eleven", 12: "twelve", 20: "twenty", 30: "thirty", 40: "fourty", 50: "fifty",
               60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
    for i in [2,3,4,5,6,7,8,9]:
        for j in range(1, 9):
            num = str(i)+"0"
            numbers[int(num)+j] = numbers[int(num)] + "-" + numbers[j]
    return numbers
# print(create_dictionary())


def write_number(num):
    return create_dictionary()[num]
# print(write_number(11))  # "eleven"
# print(write_number(2))   # "two"
# print(write_number(32))  # "thirty-two"
