n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]

dx = [1, 0, -1, 0]  
dy = [0, 1, 0, -1] 
    
x, y, direction = 0, 0, 0 
num = 1
    
for _ in range(n * m):
    arr[x][y] = num
    num += 1
        
    nx = x + dx[direction]
    ny = y + dy[direction]
        
    if nx < 0 or nx >= n or ny < 0 or ny >= m or arr[nx][ny] != 0:
        direction = (direction + 1) % 4  
        nx = x + dx[direction]
        ny = y + dy[direction]
        
    x, y = nx, ny
    
for row in arr:
    print(" ".join(map(str, row)))