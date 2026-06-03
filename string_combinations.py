from itertools import combinations

s = input()

for r in range(1, len(s) + 1):
    for c in combinations(s, r):
        print("".join(c))
