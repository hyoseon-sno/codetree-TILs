n = int(input())

def func01(n):
    if n == 0:
        return 0
    else:
        return func01(n // 10) + (n % 10) ** 2

result = func01(n)
print(result)