a,b=map(int,input().split())

def func01(a,b):
    if a>b:
        a*=2
        b+=10
    else:
        b*=2
        a+=10
    print(a,b)

func01(a,b)