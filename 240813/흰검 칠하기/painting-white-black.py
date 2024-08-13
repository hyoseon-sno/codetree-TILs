# n=int(input())
# arr = [0] * (n * 10 * 2)
# arr_c = [0] * (n * 10 * 2)
# x = n * 10-1

# for i in range(n):
#     a, b = tuple(input().split())
#     a = int(a)
#     if b == "R":
#         for j in range(x, x + a):
#             arr[j] += 1
#             arr_c[j] = "B"
#         x=x+a-1
#     elif b == "L":
#         for j in range(x, x - a, -1):
#             arr[j] += 1
#             arr_c[j] = "W"
#         x -= a
#         x=x+1

# for k in range(len(arr)):
#     if arr[k]>3:
#         arr_c[k]="G"

# x=arr_c.count("W")
# y=arr_c.count("B")
# z=arr_c.count("G")

# print(x,y,z)

n = int(input())  # 명령의 개수 입력
tiles = {}  # 각 타일의 상태를 저장할 딕셔너리
cur_pos = 0  # 현재 위치

# 각 명령을 처리
for _ in range(n):
    x, direction = input().split()
    x = int(x)

    if direction == "L":  # 왼쪽으로 이동하며 흰색으로 칠함
        for i in range(cur_pos, cur_pos - x, -1):
            if i in tiles:
                if tiles[i] == 'B':  # 이미 검은색이라면 회색으로 바꿈
                    tiles[i] = 'G'
                elif tiles[i] == 'W':  # 이미 흰색인 경우 흰색 한 번 더 칠함
                    tiles[i] = 'WW'
                elif tiles[i] == 'BB':  # 검은색 두 번 칠해진 상태에서 흰색으로 두 번 칠해진 경우
                    tiles[i] = 'G'
            else:
                tiles[i] = 'W'  # 처음 칠하는 경우 흰색으로 칠함
        cur_pos -= x  # 위치 업데이트

    elif direction == "R":  # 오른쪽으로 이동하며 검은색으로 칠함
        for i in range(cur_pos, cur_pos + x):
            if i in tiles:
                if tiles[i] == 'W':  # 이미 흰색이라면 회색으로 바꿈
                    tiles[i] = 'G'
                elif tiles[i] == 'B':  # 이미 검은색인 경우 검은색 한 번 더 칠함
                    tiles[i] = 'BB'
                elif tiles[i] == 'WW':  # 흰색 두 번 칠해진 상태에서 검은색으로 두 번 칠해진 경우
                    tiles[i] = 'G'
            else:
                tiles[i] = 'B'  # 처음 칠하는 경우 검은색으로 칠함
        cur_pos += x  # 위치 업데이트

# 흰색, 검은색, 회색 타일 수를 계산
white_count = sum(1 for color in tiles.values() if color == 'W' or color == 'WW')
black_count = sum(1 for color in tiles.values() if color == 'B' or color == 'BB')
gray_count = sum(1 for color in tiles.values() if color == 'G')

print(white_count, black_count, gray_count)