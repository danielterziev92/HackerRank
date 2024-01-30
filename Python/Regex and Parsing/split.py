import sys
from io import StringIO

test1 = '''100,000,000.000'''

sys.stdin = StringIO(test1)

import re

regex_pattern = r'[,.]'
print("\n".join(re.split(regex_pattern, input())))
