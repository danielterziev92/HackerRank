import sys
from io import StringIO

test1 = '''6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456
'''

sys.stdin = StringIO(test1)

import re


def is_valid_credit_card(card_number):
    if not re.match(r'^[4-6]', card_number):
        return False

    if not re.match(r'^\d{16}$', card_number.replace('-', '')):
        return False

    if not re.match(r'^[4-6]\d{3}(-?\d{4}){3}$', card_number):
        return False

    if re.search(r'(\d)(-?\1-?){3,}', card_number):
        return False

    return True


if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        card_number = input()
        if is_valid_credit_card(card_number):
            print("Valid")
        else:
            print("Invalid")
