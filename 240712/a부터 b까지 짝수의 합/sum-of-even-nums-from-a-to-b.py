a,b=map(int,input().split())
count=0

for i in range(a,b+1):
    if i%2==0:
        count=count+i

print(count)