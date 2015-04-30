"""
Small script for scraping words and definitions from an html page and
turning them into a JSON object.
"""

import re
from bs4 import BeautifulSoup

html = []
with open("latin.html","r") as f:
    html = f.read()

# filter out just strings with forms and meanings
soup = BeautifulSoup(html)
lines = soup.get_text().split("\n")
pairs = []
for i,v in enumerate(lines):
    if i is not len(lines)-1 and ":" in v and \
    len(lines[i+1]) is not 0 and lines[i+1][0] == " ":
        pairs.append( (v.replace(":","").strip(),lines[i+1].strip()) )

with open("latin.json","w") as out:
    out.write("[\n")
    for x in pairs:
        out.write(" "*4 + "{\n")
        out.write(" "*8 + "\"form\": \"%s\",\n" % x[0].replace('"','\\"'))
        out.write(" "*8 + "\"def\": \"%s\"\n" % x[1].replace('"','\\"'))
        out.write(" "*4 + "},\n")
    out.write("]\n")
