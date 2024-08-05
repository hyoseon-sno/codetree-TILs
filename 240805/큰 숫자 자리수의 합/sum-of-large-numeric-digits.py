a,b,c=map(int,input().split())
x=a*b*c

def func01(x):
    if x<10:
        return x
    return func01(x//10)+x%10

result=func01(x)
print(result)