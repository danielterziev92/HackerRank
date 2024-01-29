import sys
from io import StringIO

test1 = '''10
10'''

test2 = '''20
10'''

sys.stdin = StringIO(test2)

import math


def find_angle(ab, bc):
    angle_radians = math.atan2(ab, bc)
    angle_degrees = math.degrees(angle_radians)

    return round(angle_degrees)


AB_side = float(input())
BC_side = float(input())

print(str(find_angle(AB_side, BC_side)) + chr(176))
