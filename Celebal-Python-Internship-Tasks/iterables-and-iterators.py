#Calculate probability from combinations using itertools.
from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

combs = list(combinations(letters, k))
a_count = sum(1 for comb in combs if 'a' in comb)
print("{0:.3f}".format(a_count / len(combs)))
