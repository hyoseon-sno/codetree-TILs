n = int(input())
color_grid = [[0] * 201 for _ in range(201)]

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())

    x1 += 100
    y1 += 100
    x2 += 100
    y2 += 100
    
    color_code = (i % 2) + 1 
    
    for x in range(x1, x2):
        for y in range(y1, y2):
            color_grid[x][y] = color_code

blue_area = 0

for x in range(201):
    for y in range(201):
        if color_grid[x][y] == 2:
            blue_area += 1

print(blue_area)