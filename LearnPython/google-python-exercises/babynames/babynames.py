#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
from bs4 import BeautifulSoup
import sys
# import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    return


def main():
    args = sys.argv[1:]

    if not args:
        print 'usage: [--summaryfile] file [file ...]'
        sys.exit(1)
    fname = open(args[0], 'r')
    html = fname.read()
    parsed_html = BeautifulSoup(html, 'html.parser')
    year_string = parsed_html.body.find('h3').text
    remove_list = ['popularity', 'in']
    year_word_list = year_string .split()
    year = ' '.join(
      [i for i in year_word_list if i.lower() not in remove_list])
    print year
    table = parsed_html.body.find('table', attrs={'bordercolor': '#aaabbb'})
    rows = table.find_all('tr', attrs={'align': 'right'})
    for row in rows:
        for cell in row.find_all('td'):
            print 'args'
            print cell.get_text()

if __name__ == '__main__':
    main()
