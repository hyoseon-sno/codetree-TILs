n=int(input())
count=0
arr=[]

for i in range(1,11):
    arr.append(i*n)
    if (n*i) % 5 == 0:
        count +=1
    if count == 2:
        break;

for i in range(len(arr)):
    print(arr[i], end=" ")