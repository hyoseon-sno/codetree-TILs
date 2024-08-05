n = int(input())
arr = list(map(int, input().split()))

current_numbers = []

for i in range(n):
    current_numbers.append(arr[i])
    current_numbers.sort()
    if i % 2 == 0:
        median = current_numbers[i // 2]
        print(median, end=" ")