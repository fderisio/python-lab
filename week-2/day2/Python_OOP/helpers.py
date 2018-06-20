from husky import Husky


def husky_generator(num_of_dogs):
    dogs = []
    for i in range(num_of_dogs):
        dogs.append(Husky())
    return dogs
