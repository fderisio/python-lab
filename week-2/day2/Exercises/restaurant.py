class Ingredient:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __str__(self):
        return f'Ingredient: {self.name} - cost: CHF {self.cost}'


class Dish:

    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def __str__(self):
        return f'Dish name: {self.name} - price: CHF {self.price}'
    # def __iter__(self):
    #     for ingredient in self.ingredients:
    #         yield ingredient

    def cost(self):
        dish_cost = 0
        for ingredient in self.ingredients:
            dish_cost += ingredient.cost
        return dish_cost

    def profit(self):
        return self.price - self.cost()


class Customer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Customer: {self.name}'


class Restaurant:
    orders = {}

    def order_dish(self, dish, customer):
        if self.orders.get(customer):
            self.orders[customer].append(dish)
        else:
            self.orders[customer] = [dish]

    def print_orders(self, customer):
        for i, dish in enumerate(self.orders.get(customer)):
            print(f'Order #{i}: {dish.name} - CHF {dish.price}')

    def print_check(self, customer):
        self.print_orders(customer)
        check_total = 0
        for dish in self.orders.get(customer):
            check_total += dish.price
        print('Total: CHF' + str(check_total))
        return check_total


restaurant = Restaurant()
cheese = Ingredient("cheese", 5)
tomato = Ingredient("tomato", 2)
dough = Ingredient("dough", 3)
lettuce = Ingredient("lettuce", 1.5)
pizza = Dish("Pizza", 25, [cheese, tomato, dough])
salad = Dish("Salad", 19, [lettuce, cheese, tomato])
goofy = Customer('Goofy')
pluto = Customer('Pluto')
print(pizza.cost())
print(pizza.profit())
restaurant.order_dish(pizza, pluto)
restaurant.order_dish(salad, pluto)
restaurant.order_dish(pizza, pluto)
# restaurant.print_orders(pluto)
restaurant.print_check(pluto)



