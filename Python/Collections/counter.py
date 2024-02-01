import sys
from io import StringIO

test1 = '''10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50'''

sys.stdin = StringIO(test1)

if __name__ == '__main__':
    x = int(input())
    shoe_sizes = list(map(int, input().split()))
    customers = int(input())

    money = list()
    for customer in range(customers):
        shoe_size, price = map(int, input().split())
        if shoe_size in shoe_sizes:
            shoe_sizes.remove(shoe_size)
            money.append(price)

    print(sum(money))
