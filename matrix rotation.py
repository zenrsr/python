def rotation(x):
    matrix = []
    for i in range(len(x)):
        col = []
        for j in x:
            col.append(j[i])
        matrix.append(col[::-1])
    return matrix


def update(x, a, b, c):
    matrix = x.copy()
    matrix[a][b] = c
    return matrix


n = int(input())
x = []
queries = []
for i in range(n):
    x.append(list(map(int, input().split())))
original_matrix = x
while True:
    query_input = input()
    if query_input == "-1":
        break
    else:
        queries.append(query_input)

new_matrix = original_matrix
count = 0
for i in queries:
    if i[0] == "R":
        count += int(i[1:])
        angle = int("".join(i[1:]))
        for j in range(angle // 90):
            new_matrix = rotation(new_matrix)
    elif i[0] == "U":
        num = list(map(int, i[1:].split()))
        new_matrix = update(original_matrix, num[0], num[1], num[2])
        for i in range(count//90):
            new_matrix = rotation(new_matrix)
    elif i[0] == "Q":
        values = list(map(int, i[1:].split()))
        print(new_matrix[values[0]][values[1]])

    #done
