# n=int(input())
# arr = [0] * (n * 10 * 2)
# x = n * 10

# for i in range(n):
#     a,b=tuple(input().split())
#     a=int(a)
#     if b=="R":
#         for j in range(x+1,x+a+1):
#             arr[j]=arr[j]+1
#         x=x+a
#     elif b=="L":
#         for j in range(x-1,x-a-1,-1):
#             arr[j]+=1
#         x=x-a

# count=0
# for num in arr:
#     if num>1:
#         count+=1

# print(count)

n = int(input())
arr = [0] * (n * 10 * 10)  # 충분히 큰 배열 생성
x = n * 10 * 5  # 시작 위치 설정 (중간에 위치)

for _ in range(n):
    a, b = input().split()
    a = int(a)
    if b == "R":
        for j in range(x + 1, x + a + 1):  # 시작 위치 제외하고 그 다음 위치부터 업데이트
            arr[j] += 1
        x += a  # 위치 이동
    elif b == "L":
        for j in range(x - 1, x - a - 1, -1):  # 시작 위치 제외하고 그 다음 위치부터 업데이트
            arr[j] += 1
        x -= a  # 위치 이동

# 2번 이상 지나간 영역의 크기 계산
count = sum(1 for num in arr if num > 1)

print(count)