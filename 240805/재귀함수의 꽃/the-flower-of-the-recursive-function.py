n = int(input())

def func01(n):
    if n == 0:
        return

    print(n, end=" ")
    func01(n - 1)
    print(n, end=" ")


func01(n);