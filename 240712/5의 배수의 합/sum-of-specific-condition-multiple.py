a,b=map(int,input().split())
count=0

for i in range(a,b+1):
    if i%5==0:
        count+=i

print(count)