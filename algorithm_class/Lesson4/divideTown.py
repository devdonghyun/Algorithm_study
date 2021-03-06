def inRange(x, y):
    return 0 <= x < n and 0 <= y < n


def inTown(x, y):
    if not inRange(x, y):
        return False
    if grid[x][y] == 0 or visited[x][y] == 1:
        return False
    return True


def countCitizen(x, y):
    global count
    d_x, d_y = [0, 1, 0, -1], [1, 0, -1, 0]

    for i in range(4):
        new_x = x + d_x[i]
        new_y = y + d_y[i]

        if inTown(new_x, new_y):
            count += 1
            visited[new_x][new_y] = 1
            countCitizen(new_x, new_y)

    return count


n = int(input())
grid = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    grid.append(row)
visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]
citizenList = []
count = 0
for i in range(n):
    for j in range(n):
        if inTown(i, j):
            count = 1
            visited[i][j] = 1
            countCitizen(i, j)
            citizenList.append(count)

citizenList.sort()
length = 0

for citizen in citizenList:
    if citizen != 0:
        length += 1
print(length)
for citizen in citizenList:
    if citizen != 0:
        print(citizen)

# print([citizenList[i] for i in range(len(citizenList)) if citizenList[i] != 0])
