class Car:
    def __init__(self, color, tank_size, laps, lap_length):
        self.color = color
        self.tank_size = tank_size
        self.laps = laps
        self.lap_length = lap_length

    def special_method(self, kwargs):
        return kwargs

    def run_laps(self):
        return self.tank_size/self.laps

    def check_pit_stop(self):
        if tank_size <= 10:
            return "pull in for a pit stop and re-fill the tank"


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'{self.title} by {self.author}'


class BookShelf:
    books = []

    def __init__(self, books=None):
        for book in books:
            books.append(Book(book[0], book[1]))


book_shelf = BookShelf(books=[
    ('The old man and the see', 'Ernest Hemingway'),
    ('Beyond Good and Evil', 'Friedrich Nietzsche'),
])

print(book_shelf)

