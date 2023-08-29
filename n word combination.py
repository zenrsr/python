from itertools import combinations


def unique(words, n):
    x = []
    words = sorted(words)
    for i in combinations(words, n):
        x.append(i)
    x = sorted(set(x))
    for k in x:
        print(" ".join(k))


words = (input().split())
n = int(input())
unique(words, n)