n = int(input())
arr=[]

for i in range(n):
    x,y=map(int,input().split())
    arr.append((abs(x)+abs(y),i+1))

arr.sort(key=lambda x: (x[0],x[1]))

for a in arr:
    print(a[1])