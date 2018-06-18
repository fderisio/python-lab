# New comment

example = 'This is a variable'  # comment after 2 spaces

""""Multi lines
....
comment """


def multiply():
    number = 9  # indentation: 4 spaces
    return number


new_number = multiply()


def multiply_with_params(num1, num2):  # solo acepta numeros
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


print(type(divide(num1=10, num2=5)))
print(int(divide(10, 5)))
print(str(divide(10, 5)))
print(float(100))


print(bool(1))
print(bool(False))
# 2 lines spaces


class Example:
    # one line space only
    def method1(self):
        return 'hola'

    def method2(self):
        return "chau"


if multiply_with_params(2,4):
    print("hello")
else:
    print("nope")

counter = 0
while counter>10:
    if counter == 2:
        counter += 1
        continue
    print(counter)  # imprime todo menos el dos


for i in range(1, 100):
    print(i)
    if i == 10:
        break

my_list = [1,2,3,4,5]
my_list.insert(0,100)  # inserts in index 0
my_list.remove(100)
my_list.clear()
my_list.append(200)  # appends at the end of the list
my_list.sort()  # does not return anything, it cant be printed
print(sorted(my_list, reverse=True))  # sorted RETURN something! That's why can be printed
my_list.reverse()
my_list.count(2)  # cuenta cuantas veces esta el 2 en la lista


people = [{
    'name': 'Laurent',
    'age': 26,
}]

print(people[0]['name'])
# print(people[0]['hair_color'])  # sale del codigo!

people[0]['hair_color'] = 'brown'  # agrega una propiedad nueva

for key in people[0].keys():
    print("the key is", key)


for value in people[0].values():
    print(value)


for key, value in people[0].items():
    print(f'{key} => {value}')


def give_me_back_a_tuple():
    return '1', '2', '3'


my_result = give_me_back_a_tuple()
one, two, three = give_me_back_a_tuple()
print(my_result)
print(one)

