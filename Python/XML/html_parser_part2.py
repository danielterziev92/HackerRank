import sys
from io import StringIO

test1 = '''4
<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->
'''

sys.stdin = StringIO(test1)

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        lines = data.split('\n')
        if len(lines) == 1:
            print(">>> Single-line Comment")
            print(lines[0])
        else:
            print(">>> Multi-line Comment")
            for line in lines:
                print(line)

    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)


if __name__ == "__main__":
    n = int(input().strip())  # Number of lines

    html_lines = []
    for _ in range(n):
        line = input().strip()
        html_lines.append(line)

    html_code = "\n".join(html_lines)

    parser = MyHTMLParser()
    parser.feed(html_code)
