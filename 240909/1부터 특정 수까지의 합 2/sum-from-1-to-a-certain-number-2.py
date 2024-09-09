n=int(input())

def func01(n):
    if n==0:
        return 0
    return func01(n-1)+n
    
print(func01(n))