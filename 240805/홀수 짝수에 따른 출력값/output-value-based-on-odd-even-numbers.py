def sum_odd(n):
    if n == 1:
        return 1
    return n + sum_odd(n - 2)

def sum_even(n):
    if n == 2:
        return 2
    return n + sum_even(n - 2)

n = int(input())

if n % 2 == 0:
    result = sum_even(n)
else:
    result = sum_odd(n)

print(result)