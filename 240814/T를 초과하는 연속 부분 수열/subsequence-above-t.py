n, t = map(int, input().split())
arr = list(map(int, input().split()))

max_length = 0
current_length = 0

for num in arr:
    if num > t:
        current_length += 1
        if current_length > max_length:
            max_length = current_length
    else:
        current_length = 0

print(max_length)