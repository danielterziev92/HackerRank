import sys
from io import StringIO

test1 = 'BANANA'

sys.stdin = StringIO(test1)


def minion_game(string):
    vowels = "AEIOU"
    stuart_score = 0
    kevin_score = 0
    length = len(s)

    for i in range(length):
        if s[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i

    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
