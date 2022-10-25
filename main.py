"""
Programček, ki pomaga pri iskanju besed za besedovnjak in pri hitrem iskanju
uporablja trie.
[https://en.wikipedia.org/wiki/Trie]
"""

# includes
import csv
import pygtrie

# load and learn trie
t = pygtrie.CharTrie()

# read the list of words
with open('sbsj.csv', encoding="utf8", newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        s = str(row[0].upper())
        if (len(s) < 5):
            continue
        t[s] = True

# create array (4x4 characters)
letters = 'AKČSAAOPKAOVLJZT'

# building the 4x4 matrix
i = 0
j = 0

l = []
r = []
m = []

rx = []
mx = []

for j in range(len(letters)):
    r.append(letters[j])
    rx.append(0)
    if (j % 4 == 3):
        m.append(r)
        r = []
        mx.append(rx)
        rx = []

# direction matrix for the next move
direction = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1], [0, 1],
    [1, -1], [1, 0], [1, 1]
]

# vector of words
words = []

def addW(w):
    """
    Add a word to the list if it does not yet exist inside.
    """
    if w not in words:
        words.append(w)

# recursive function to transverse the array
def search(x, y, w, mx):
    w = w + m[x][y]

    value = t.get(str(w))
    #print(w)
    if value is not None:
        #print("FOUND!", repr(w))
        addW(w)
    if not t.has_subtrie(w):
        return

    if (len(w) == 11):
        return(x)

    for d in direction:
        mxx = mx.copy()
        nx = x + d[0]
        ny = y + d[1]

        if (nx > 3) or (ny > 3) or (nx < 0) or (ny < 0):
            continue

        if (mx[nx][ny] == 1):
            continue

        mxx[x][y] = 1

        # print(nx, ny, w, mx)
        search(nx, ny, w, mxx)
        mxx[x][y] = 0

# running recursion for each start letter
for i in range(4):
    for j in range(4):
        # print(i, j)
        search(i, j, '', mx[:])

words.sort(key = lambda s: -len(s))
print(words)