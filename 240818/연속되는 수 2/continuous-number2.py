N=int(input())

arr=[]
count=0
result=[]

for _ in range(N):
    x=int(input())
    arr.append(x)

if N>1:
    for i in range(1,N):
        if arr[i-1]==arr[i]:
            count+=1
        if arr[i-1]!=arr[i]:
            result.append(count+1)
if N==1:
    result.append(1)



if len(result)!=0:
    print(max(result)) 
else:
    print(0)