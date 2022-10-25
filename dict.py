# load csv
import csv
import pygtrie

t = pygtrie.CharTrie()

with open('sbsj.csv', encoding="utf8", newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        s = str(row[0].upper())
        t[s] = True

text = 'SREČA'
value = t.get(text)

if value is not None:
    print(repr(text), 'is a word')
if t.has_subtrie(text):
    print(repr(text), 'is a prefix of a word')
else:
    print(repr(text), 'is not a prefix, going back to empty string')
    text = ''