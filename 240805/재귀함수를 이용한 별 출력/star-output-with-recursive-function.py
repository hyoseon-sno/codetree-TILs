n=int(input())

def func01(n):
    if n==0:
        return
    func01(n-1)
    print("*"*n)

func01(n)