from helpers import husky_generator


class Slider:
    min_strength = 20
    meters_moved = 0

    def __init__(self, huskies):
        self.huskies = huskies

    def get_applied_strength(self):
        return sum([h.strength for h in self.huskies])

    def move(self):
        if self.get_applied_strength() < self.min_strength:
            print("Slider can't be moved!")
        else:
            self.meters_moved += 1
        return self.meters_moved


if __name__ == '__main__':
    slider = Slider(huskies=husky_generator(10))
    print(slider.get_applied_strength())
    slider.move()
