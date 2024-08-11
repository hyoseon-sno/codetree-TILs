m1, d1, m2, d2 = map(int, input().split())

month_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_name = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

total_days = 0

if (m1 > m2) or (m1 == m2 and d1 > d2):
    total_days += d2 - d1
    
    for i in range(m2, m1):
        total_days -= month_day[i]

    if m1 != m2:
        total_days -= month_day[m1] - d1

else:
    if m1 == m2:
        total_days = d2 - d1
    else:
        total_days += month_day[m1] - d1
        for i in range(m1 + 1, m2):
            total_days += month_day[i]
        total_days += d2

index = total_days % 7

index = (7 + index) % 7

print(day_name[index])