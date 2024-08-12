n=int(input())
arr = [0] * (n * 10 * 2)
arr_c = [0] * (n * 10 * 2)
x = n * 10-1

for i in range(n):
    a, b = tuple(input().split())
    a = int(a)
    if b == "R":
        for j in range(x, x + a):
            arr[j] += 1
            arr_c[j] = "B"
        x=x+a-1

    elif b == "L":
        for j in range(x, x - a, -1):
            arr[j] += 1
            arr_c[j] = "W"
        x -= a
        x=x+1


for k in range(len(arr)):
    if arr[k]>3:
        arr_c[k]="G"

x=arr_c.count("W")
y=arr_c.count("B")
z=arr_c.count("G")

print(x,y,z)