from dogs import Dog


class Husky(Dog):
    max_strength = 10

    @property
    def strength(self):
        return self.max_strength / self.age

    def __str__(self):
        return f'{super().__str__()}, strength: {self.strength}'


if __name__ == '__main__':

    husky1 = Husky('Jessy', 5, strength=9)
    print(husky1)
    print(husky1.strength)
    print(husky1.__dict__)
