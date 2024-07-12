n=int(input())
a=1

for i in range(1,11):
    a=a*i
    if a==n or a>n:
        print(i)
        break