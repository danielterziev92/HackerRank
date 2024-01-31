import sys
from io import StringIO

test1 = '''11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}   
'''

sys.stdin = StringIO(test1)

import re


def extract_hex_color_code(text):
    pattern = r'#(?:[0-9a-fA-F]{3}){1,2}\b(?![^{}]*\{[^{}]*\})'
    return re.findall(pattern, text)


if __name__ == '__main__':
    n = int(input())

    lines = []
    for _ in range(n):
        line = input()
        lines.append(line)
    # Cab
    hex_colors = extract_hex_color_code(''.join(lines))

    print(*hex_colors, sep='\n')
