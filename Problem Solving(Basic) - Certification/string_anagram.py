import sys
from io import StringIO

test1 = '''5
heater
cold
clod
reheat
docl
3
codl
heater
abcd'''

sys.stdin = StringIO(test1)


def stringAnagram(dictionary, query):
    freq_dict = dict()

    for word in dictionary:
        sorted_word = ''.join(sorted(word))
        freq_dict[sorted_word] = freq_dict.get(sorted_word, 0) + 1

    result = [freq_dict.get(''.join(sorted(q)), 0) for q in query]

    return result


if __name__ == '__main__':
    dictionary_count = int(input().strip())

    dictionary = []

    for _ in range(dictionary_count):
        dictionary_item = input()
        dictionary.append(dictionary_item)

    query_count = int(input().strip())

    query = []

    for _ in range(query_count):
        query_item = input()
        query.append(query_item)

    result = stringAnagram(dictionary, query)

    print('\n'.join(map(str, result)))
