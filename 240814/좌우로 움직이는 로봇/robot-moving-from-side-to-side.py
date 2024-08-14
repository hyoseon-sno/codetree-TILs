n, m = map(int, input().split())

pos_a, pos_b = 0, 0

pos_a_list, pos_b_list = [], []

for _ in range(n):
    t, d = input().split()
    t = int(t)
    for _ in range(t):
        if d == 'L':
            pos_a -= 1
        elif d == 'R':
            pos_a += 1
        pos_a_list.append(pos_a)

for _ in range(m):
    t, d = input().split()
    t = int(t)
    for _ in range(t):
        if d == 'L':
            pos_b -= 1
        elif d == 'R':
            pos_b += 1
        pos_b_list.append(pos_b)

while len(pos_a_list) < len(pos_b_list):
    pos_a_list.append(pos_a)
while len(pos_b_list) < len(pos_a_list):
    pos_b_list.append(pos_b)

result = 0
for t in range(1, len(pos_a_list)):
    if pos_a_list[t] == pos_b_list[t] and pos_a_list[t-1] != pos_b_list[t-1]:
        result += 1

print(result)