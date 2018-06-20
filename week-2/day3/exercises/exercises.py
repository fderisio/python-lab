import random


def even(some_list):
    return list(filter(lambda x: x % 2 == 0, some_list))


def calculate_square(some_list):
    return list(map(lambda x: x ** 2, some_list))


def calculate_square_even(some_list):
    return even(calculate_square(some_list))


list1 = [1,2,3,4,5,6,7,8,9,10]
print(even(list1))
print(calculate_square(list1))
print(calculate_square_even(list1))


def find_numbers(min, max):
    new_list = list(x for x in range(min, max+1))
    return list(filter(lambda x: x % 7 == 0 and x % 5 != 0, new_list))


print(find_numbers(1,35))


def increase(quantity, price):
    if quantity * price > 100:
        return (quantity * price) + 10
    else:
        return quantity * price


def compute_totals(some_orders):
    return list(map(lambda x: (x['id'], increase(x['quantity'], x['price_per_item'])), some_orders))


orders = [
    {
        'id': 'order_001',
        'item': 'Introduction to Python',
        'quantity': 1,
        'price_per_item': 32,
    },
    {
        'id': 'order_002',
        'item': 'Advanced Python',
        'quantity': 3,
        'price_per_item': 40,
    },
    {
        'id': 'order_003',
        'item': 'Python web frameworks',
        'quantity': 2,
        'price_per_item': 51,
    },
]
# print(compute_totals(orders))


def generator(num):
    return {x: x ** 2 for x in range(1, num)}
# print(generator(10))


def print_even(num):
    filtered = list(filter(lambda x: x % 2 == 0, num))
    return ''.join('_' + str(x) for x in filtered)


print(print_even(list1))


def bmi_result(num):
    if num < 18.5:
        print('Underweight')
    if 18.5 >= num <= 25:
        print('Normal')
    if num > 25:
        return 'Overweight'


def bmi_calculator():
    height = int(input('What is your height (in CM)?'))
    weight = float(input('What is your weight (in KG)?'))
    bmi = round(weight / ((height / 100) ** 2), 2)
    print('Your BMI is:', bmi, bmi_result(float(bmi)))
    return bmi
# bmi_calculator()


def help_menu():
    print('Press \'h\' for help menu \n '
          'Press \'s\' to show the item in your list \n '
          'Press \'a\' to add a new item to the list \n '
          'Press \'r\' to remove an item from the list \n '
          'Press \'q\' to quit')


def show_items(items_list):
    print('The new items on the list are:', items_list)


def add_item(items_list, new_item):
    items_list.append(new_item)


def remove_item(items_list, item):
    items_list.remove(item)
    print('The new items on the list are:', items_list)


def options_menu():
    user_active = True
    user_list = []
    help_menu()
    while user_active:
        option = input('What would you like to do?')
        if option == 'h':
            help_menu()
        if option == 's':
            show_items(user_list)
        if option == 'a':
            new_item = input('What item would you like to add?')
            add_item(user_list, new_item)
        if option == 'r':
            item = input('What item would you like to remove?')
            remove_item(user_list, item)
        if option == 'q':
            print('Goodbye!')
            user_active = False

# options_menu()

# --------------------- #


def play_again():
    start()


def start():
    user_guesses = 5
    print('I\'m thinking a number between 1-10')
    random_num = random.randint(1, 10)
    print('You have 5 chances')
    while user_guesses > 0:
        guess = int(input('Enter a number:'))
        if guess == random_num:
            print('You win!')
            break
        else:
            user_guesses -= 1
    else:
        print('You lose! The number was:', random_num)
    option = str(input('Would you like to play again(Y/N)?'))
    if option == 'n':
        print('Goodbye!')
    if option == 'y':
        return play_again()

# start()