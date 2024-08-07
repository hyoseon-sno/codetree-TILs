n=int(input())
arr=list(map(int,input().split()))

a=[]
b=[]
used = [False] * n

for i in range(n):
    a.append((arr[i], i+1))

arr.sort()

for i in range(n):
    b.append((arr[i],i+1))

result = [0] * n  

for j in range(n):
    for k in range(n):
        if a[j][0] == b[k][0] and not used[k]: 
            result[j] = b[k][1]
            used[k] = True
            break

print(" ".join(map(str, result)))