n = int(input())
arr = [[0 for _ in range(300)] for _ in range(300)]

x, y = 100,100

for _ in range(n):
    a, b = map(int, input().split())
    x += a
    y += b
    for i in range(x, x + 8):
        for j in range(y, y + 8):
            arr[i][j] = 1  

result = 0
for i in range(300):
    for j in range(300):
        if arr[i][j] == 1:
            result += 1

print(result)