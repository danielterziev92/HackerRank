import sys
from io import StringIO

test1 = '''9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>

'''

sys.stdin = StringIO(test1)

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

    def handle_comment(self, data):
        pass


if __name__ == "__main__":
    n = int(input())

    html_lines = []
    for _ in range(n):
        line = input()
        html_lines.append(line)

    html_code = "\n".join(html_lines)

    parser = MyHTMLParser()
    parser.feed(html_code)
