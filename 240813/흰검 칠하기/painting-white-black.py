n=int(input())
arr = [0] * (20000 + 1) 
arr_c = [" "] * (20000 + 1)
x = 10000  

for i in range(n):
    a, b = input().split()
    a = int(a)
    if b == "R":
        for j in range(x, x + a):
            arr[j] += 1
            arr_c[j] = "B"
        x = x + a - 1  
    elif b == "L":
        for j in range(x, x - a, -1):
            arr[j] += 1
            arr_c[j] = "W"
        x = x - a
        x = x + 1  
for gray in range(len(arr)):
    if arr[gray] > 3:
        arr_c[gray] = "G"

x = arr_c.count("W")
y = arr_c.count("B")
z = arr_c.count("G")

print(x, y, z)