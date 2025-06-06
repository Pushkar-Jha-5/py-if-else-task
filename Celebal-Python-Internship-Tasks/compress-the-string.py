#Compress consecutive characters with counts using itertools.groupby
from itertools import groupby

s = input()
compressed = [(len(list(g)), int(k)) for k, g in groupby(s)]
print(*compressed)
