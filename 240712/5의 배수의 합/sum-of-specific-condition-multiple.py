a, b = map(int, input().split())
count = 0

start = min(a, b)
end = max(a, b)

for i in range(start, end + 1):
    if i % 5 == 0:
        count += i

print(count)