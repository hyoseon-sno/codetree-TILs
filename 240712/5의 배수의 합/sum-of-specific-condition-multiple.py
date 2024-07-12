a,b=map(int,input().split())
count=0

for i in range(a+1,b):
    if i%5==0:
        count+=i

print(count)