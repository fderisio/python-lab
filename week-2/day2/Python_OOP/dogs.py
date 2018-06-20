import names
import random


class Dog:
    origin = 'US'
    possible_gender = ['male', 'female']

    def __init__(self, name=None, gender=None, age=None, **kwargs):
        self.name = name
        # check gender
        if gender in self.possible_gender:
            self.gender = gender
        else:
            self.gender = self.generate_gender()

        # if no name, generate a name
        if not self.name:
            self.name = self.generate_name(self.gender)
        self.tricks = kwargs.get('tricks')
        self.age = age if age else random.randint(1, 14)
        self.origin = kwargs.get('origin', self.origin)

    def generate_gender(self):
        return self.possible_gender[random.randint(0,1)]

    def generate_name(self, gender='male'):
        return names.get_first_name(gender=gender)

    def __str__(self):
        return f'name: {self.name}, age: {self.age}, origin: {self.origin}'

    def __len__(self):
        return len(self.__dict__)

    def __int__(self):
        return int(self.age)

    def __float__(self):
        return float(self.age)

    def __iter__(self):
        for trick in self.tricks:
            yield trick

if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    dog_generator = {
        'name': 'Juka',
        'age': 9,
        'origin': 'CH',
        'tricks': ['roll over', 'play dead'],
        'color': 'brown-white',
    }
    dog1 = Dog(**dog_generator)

    print(str(dog1))
    print('Len of the dog: ', len(dog1))
    print('Age of the dog: ', int(dog1))
    print('Float Age of the dog: ', float(dog1))

    dog_trick_generator = iter(dog1)
    print(dog_trick_generator)
    for trick in dog1:
        print(trick)
