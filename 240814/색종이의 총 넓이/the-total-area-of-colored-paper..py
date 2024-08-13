n = int(input())
arr = [[0 for _ in range(200)] for _ in range(200)]
x, y = 99,99

for _ in range(n):
    a, b = map(int, input().split())
    x += a
    y += b
    for i in range(x, x + 8):
        for j in range(y, y + 8):
            arr[i][j] = 1 

result = 0
for i in range(200):
    for j in range(200):
        if arr[i][j] == 1:
            result += 1

print(result)