n,k,T=tuple(input().split())

arr = [input() for _ in range(int(n))]
arr = [i for i in arr if i.startswith(T)]

arr.sort()
print(arr[int(k)-1])