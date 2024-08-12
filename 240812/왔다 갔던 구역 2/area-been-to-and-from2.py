# n=int(input())
# arr = [0] * (n * 10 * 2)
# x = n * 10

# for i in range(n):
#     a,b=tuple(input().split())
#     a=int(a)
#     if b=="R":
#         for j in range(x,x+a):
#             arr[j]=arr[j]+1
#         x=x+a
#     elif b=="L":
#         for j in range(x,x-a,-1):
#             arr[j]+=1
#         x=x-a

# count=0
# for num in arr:
#     if num>1:
#         count+=1

# print(count)

n = int(input())
# 충분히 큰 크기의 배열 생성, 중간에 x=0을 배치하기 위해 n*10*2
arr = [0] * (n * 10 * 2)
# 시작 위치 설정 (중간에 위치)
x = n * 10

for _ in range(n):
    a, b = input().split()
    a = int(a)
    if b == "R":
        for j in range(x, x + a):
            arr[j] += 1
        x += a  # 위치 이동
    elif b == "L":
        for j in range(x, x - a, -1):
            arr[j] += 1
        x -= a  # 위치 이동

# 2번 이상 지나간 영역의 크기 계산
count = sum(1 for num in arr if num > 1)

print(count)