n,m=map(int,input().split())
A=list(map(int,input().split()))

def func01(n,m,A):
    for _ in range(m):
        a1,a2=map(int,input().split())
        count=0
        for i in range(a1-1,a2):
            count+=A[i]
        print(count)

func01(n,m,A)