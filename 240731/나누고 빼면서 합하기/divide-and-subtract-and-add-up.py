def func01(m, A):
    x = 0
    while m > 0:
        x += A[m - 1]
        if m == 1:
            break
        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
    print(x)

n, m = map(int, input().split())
A = list(map(int, input().split()))

func01(m, A)