import sys
from io import StringIO

test1 = '''6
2
1 2
2 5
3 4
4 5
5 6
7 6'''

sys.stdin = StringIO(test1)

from itertools import combinations


def is_valid_hotel_set(adj_list, hotels):
    distances = set()
    for i in range(len(hotels)):
        for j in range(i + 1, len(hotels)):
            distance = shortest_path(adj_list, hotels[i], hotels[j])
            distances.add(distance)
    return len(distances) == 1


def shortest_path(adj_list, start, end):
    visited = set()
    queue = [(start, 0)]

    while queue:
        current, distance = queue.pop(0)
        visited.add(current)

        if current == end:
            return distance

        for neighbor in adj_list[current]:
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))

    return float('inf')


def numberOfWays(roads):
    adj_list = {i: [] for i in range(1, len(roads) + 2)}

    for road in roads:
        adj_list[road[0]].append(road[1])
        adj_list[road[1]].append(road[0])

    cities = list(range(1, len(roads) + 2))
    hotel_combinations = list(combinations(cities, 3))

    valid_ways = 0
    for hotels in hotel_combinations:
        if is_valid_hotel_set(adj_list, hotels):
            valid_ways += 1

    return valid_ways


if __name__ == '__main__':
    roads_rows = int(input().strip())
    roads_columns = int(input().strip())

    roads = []

    for _ in range(roads_rows):
        roads.append(list(map(int, input().rstrip().split())))

    result = numberOfWays(roads)

    print(str(result) + '\n')
