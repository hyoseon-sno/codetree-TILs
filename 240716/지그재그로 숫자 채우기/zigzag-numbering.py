a,b=map(int,input().split())

arr=[
    [0 for _ in range(b)]
    for _ in range(a)
]

x=0

for i in range(b):
    if i%2 == 0:
        for j in range(a):
            arr[j][i]=x
            x+=1
    else:
        for j in range(a-1, -1, -1):
            arr[j][i] = x
            x += 1

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()