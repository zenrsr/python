def main():
    new_list =[]
    n = list(map(int, input().split()))
    for i in range(len(n)):
        l = []
        for j in range(i,len(n)):
            main = dict()
            l.append(n[j])
            main[sum(l)] = list(l)
            new_list.append(main)
    return new_list

x = main()
keys = []
values = []
for i in x:
    # print(i)
    keys.append(sum(list(i.keys())))
    values.extend(list(i.values()))
degree = max(keys)
# print(degree)
index = keys.index(degree)
result = values[index]
result = list(map(str, result))
print(" ".join(result))