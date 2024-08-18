N=int(input())

arr=[]
count=0
result=[]

for _ in range(N):
    x=int(input())
    arr.append(x)

for i in range(1,N):
    if arr[i-1]==arr[i]:
        count+=1
    if arr[i-1]!=arr[i]:
        result.append(count+1)
        result.append(1)

print(max(result))