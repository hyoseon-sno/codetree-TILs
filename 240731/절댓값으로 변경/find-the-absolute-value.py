n=int(input())
arr=list(map(int,input().split()))

def func01(arr):
    for i in range(n):
        if arr[i]<0:
            arr[i]=arr[i]*(-1)
        else:
            continue

func01(arr)

for x in arr:
    print(x, end = " ")