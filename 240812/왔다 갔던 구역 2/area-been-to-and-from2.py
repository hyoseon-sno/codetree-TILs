n=int(input())
arr = [0] * (n * 10 * 2)
x = n * 10

for i in range(n):
    a,b=tuple(input().split())
    a=int(a)
    if b=="R":
        for j in range(x,x+a):
            arr[j]=arr[j]+1
        x=x+a
    elif b=="L":
        for j in range(x,x-a,-1):
            arr[j]+=1
        x=x-a

count=0
for num in arr:
    if num>1:
        count+=1

print(count)