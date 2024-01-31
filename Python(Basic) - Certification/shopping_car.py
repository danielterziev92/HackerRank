import sys
from io import StringIO

test1 = '''1
candy 2
5
add candy
add candy
add candy
len
total
'''

test2 = '''2
bike 1000
headphones 1000
8
total
add bike
len
total
add headphones
add headphones
len
total
'''

sys.stdin = StringIO(test2)


class Item:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.card = list()

    def add(self, item: Item):
        self.card.append(item)

    def total(self):
        return sum([item.price for item in self.card])

    def __len__(self):
        return len(self.card)


if __name__ == '__main__':
    n = int(input())
    items = []
    for _ in range(n):
        name, price = input().split()
        item = Item(name, int(price))
        items.append(item)

    cart = ShoppingCart()

    q = int(input())
    for _ in range(q):
        line = input().split()
        command, params = line[0], line[1:]
        if command == "len":
            print(str(len(cart)) + "\n")
        elif command == "total":
            print(str(cart.total()) + "\n")
        elif command == "add":
            name = params[0]
            item = next(item for item in items if item.name == name)
            cart.add(item)
        else:
            raise ValueError("Unknown command %s" % command)
