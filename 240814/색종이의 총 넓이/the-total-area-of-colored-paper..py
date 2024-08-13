n = int(input())
arr = [[0 for _ in range(200)] for _ in range(200)]

for _ in range(n):
    a, b = map(int, input().split())
    x = a + 100
    y = b + 100
    for i in range(x, x + 8):
        for j in range(y, y + 8):
            arr[i][j] = 1 


result = sum(sum(row) for row in arr)

print(result)