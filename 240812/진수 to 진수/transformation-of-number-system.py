a, b = map(int, input().split())
n = input()

def ntoten(n, a):
    result = 0
    n = n[::-1]
    for i in range(len(n)):
        result += int(n[i]) * (a ** i)
    return result

def tenton(n, b):
    result = ''
    while n > 0:
        result = str(n % b) + result
        n = n // b
    return result

x = ntoten(n, a)
if x == 0:
    print(0)
else:
    print(tenton(x, b))