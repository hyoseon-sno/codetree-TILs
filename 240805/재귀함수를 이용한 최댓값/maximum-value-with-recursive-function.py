n = int(input())
arr = list(map(int, input().split()))

def func01(arr, n):
    if n == 1:
        return arr[0]
    else:
        return max(arr[n-1], func01(arr, n-1))

result = func01(arr, n)
print(result)