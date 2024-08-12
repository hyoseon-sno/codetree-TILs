# n=int(input())
# arr = [0] * (n * 10 * 2)
# x = n * 10

# for i in range(n):
#     a, b = tuple(input().split())
#     a = int(a)
#     if b == "R":
#         for j in range(x, x + a):
#             arr[j] += 1
#         x += a
#     elif b == "L":
#         for j in range(x, x - a, -1):
#             arr[j] += 1
#         x -= a

# count = 0
# for num in arr:
#     if num > 1:
#         count += 1

# print(count)

n = int(input())
OFFSET = n * 10  # OFFSET을 n*10으로 설정
arr = [0] * (OFFSET * 2)  # 배열 크기를 넉넉하게 설정
x = OFFSET  # 시작 위치를 중앙으로 설정

for _ in range(n):
    a, b = input().split()
    a = int(a)
    if b == "R":
        for j in range(x, x + a):
            arr[j] += 1
        x += a
    elif b == "L":
        for j in range(x, x - a, -1):
            arr[j] += 1
        x -= a

count = 0
for num in arr:
    if num >= 2:  # 2번 이상 지나간 구역을 카운트
        count += 1

print(count)