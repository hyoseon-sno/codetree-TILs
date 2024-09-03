n = int(input())

def func01(n):
    if n != 0:
        print("HelloWorld")
        func01(n - 1) 

func01(n)