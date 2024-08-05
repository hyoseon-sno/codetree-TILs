n=int(input())

def func01(n):
    if n==0 or n==1:
        return 1
    
    else:
        return n*func01(n-1)

result = func01(n)
print(result)