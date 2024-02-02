import sys
from io import StringIO

test1 = '08 05 2015'

sys.stdin = StringIO(test1)

from datetime import datetime

date_string = input()

date_obj = datetime.strptime(date_string, '%m %d %Y')
print(date_obj.strftime('%A').upper())
