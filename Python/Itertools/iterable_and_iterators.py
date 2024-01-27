import sys
from io import StringIO

test1 = '''4 
a a c d
2'''

sys.stdin = StringIO(test1)


def calculate_probability(n, letters, k):
    indices_a = [i for i, letter in enumerate(letters) if letter == 'a']

    probability_not_a = 1.0
    for i in range(k):
        probability_not_a *= (n - i - len(indices_a)) / (n - i)

    probability_at_least_one_a = 1.0 - probability_not_a

    return round(probability_at_least_one_a, 4)


if __name__ == "__main__":
    n = int(input())
    letters = input().split()
    k = int(input())

    result = calculate_probability(n, letters, k)
    print(result)
