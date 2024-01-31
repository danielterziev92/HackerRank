import sys
from io import StringIO

test1 = '''2
<html><head><title>HTML Parser - I</title></head>
<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html> 
'''

sys.stdin = StringIO(test1)

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")


if __name__ == "__main__":
    n = int(input())

    html_lines = []
    for _ in range(n):
        line = input()
        html_lines.append(line)

    html_code = "\n".join(html_lines)

    parser = MyHTMLParser()
    parser.feed(html_code)
