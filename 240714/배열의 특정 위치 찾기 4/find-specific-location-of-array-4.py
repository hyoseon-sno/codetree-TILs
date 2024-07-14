arr=list(map(int,input().split()))
count,result=0,0

for i in range(10):
    if arr[i]==0:
        break;
    else:
        if arr[i] % 2==0:
            count+=1
            result+=arr[i]
        else:
            continue

print(count, result)