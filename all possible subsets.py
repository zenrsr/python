from itertools import combinations

def find(words, n):
    for i in range(1,n+1):
        x= []
        for j in combinations(words, i):
            x.append(j)
        x = sorted(set(x))
        for k in x:
            print(" ".join(k))
words = sorted(input().split())
n = len(words)
find(words, n)