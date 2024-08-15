n, m = map(int, input().split())

a_positions = []
b_positions = []

# A
current_position = 0
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        current_position += v
        a_positions.append(current_position)

# B
current_position = 0
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        current_position += v
        b_positions.append(current_position)

#변경 횟수 계산
lead = ""
changes = 0

for i in range(len(a_positions)):
    if a_positions[i] > b_positions[i]:
        current_lead = "A"
    elif a_positions[i] < b_positions[i]:
        current_lead = "B"
    else:
        current_lead = "AB"

    if current_lead != lead:
        lead = current_lead
        changes += 1

print(changes)