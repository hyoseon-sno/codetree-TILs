n=int(input())
arr=list(map(int,input().split()))

arr.sort()
for i in range(n):
    if i==0 or i%2==0:
        x=i//2
        print(arr[x],end=" ")