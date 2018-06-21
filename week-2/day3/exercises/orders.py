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


print(compute_totals(orders))
