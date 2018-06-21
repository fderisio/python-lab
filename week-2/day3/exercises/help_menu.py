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
        if option not in ['h', 's', 'a', 'r', 'q']:
            print('Please enter a valid option.')


options_menu()
