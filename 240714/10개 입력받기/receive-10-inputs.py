arr=list(map(int,input().split()))
brr=[]
result,aver,count=0,0,0

for i in range(10):
    if arr[i]==0:
        break;
    else:
        count+=1
        brr.append(arr[i])
        result=result+arr[i]
        
aver=result/count
print(f"{result} {aver:.1f}")