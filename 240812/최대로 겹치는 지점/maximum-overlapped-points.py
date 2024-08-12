n=int(input())
arr=[0 for i in range(100)]

for _ in range(n):
    a,b=map(int,input().split())
    for i in range(a,b+1):
        arr[i]=arr[i]+1

print(max(arr))