n=int(input())
data=[]

for i in range(n):
    arr=list(map(int, input().split()))
    data.append((arr[0],arr[1],i+1))

data.sort(key=lambda x: (x[0], -x[1]))

for a in data:
    print(a[0], a[1], a[2])