import sys
from io import StringIO

test1 = '''2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000'''

sys.stdin = StringIO(test1)

import math
import os
import random
import re
import sys
from datetime import datetime, timedelta


def time_delta(t1, t2):
    date_object1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    date_object2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    return str(abs(int(((date_object1 - date_object2).total_seconds()))))


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)

        print(delta)
