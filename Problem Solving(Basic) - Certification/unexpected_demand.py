import sys
from io import StringIO

test1 = '''2
10
30
40'''

sys.stdin = StringIO(test1)


def filledOrders(orders, k):
    fulfilled_order = 0
    orders.sort()
    for order in orders:
        if k - order >= 0:
            fulfilled_order += 1
            k -= order
        else:
            break

    return fulfilled_order


if __name__ == '__main__':
    order_count = int(input().strip())

    order = []

    for _ in range(order_count):
        order_item = int(input().strip())
        order.append(order_item)

    k = int(input().strip())

    result = filledOrders(order, k)

    print(result)
