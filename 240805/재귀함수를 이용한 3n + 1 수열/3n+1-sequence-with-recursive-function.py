n = int(input())

def func01(n, count=0):
    if n == 1:
        return count
    if n % 2 == 0:
        return func01(n // 2, count + 1)
    else:
        return func01(3 * n + 1, count + 1)

result = func01(n)
print(result)