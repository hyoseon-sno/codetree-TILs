m1, d1, m2, d2 = map(int, input().split())

def count_weekday_occurrences(m1, d1, m2, d2, target_day):
    month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_name = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    
    total_days = 0
    
    total_days += month_days[m1] - d1 + 1
    
    for month in range(m1 + 1, m2):
        total_days += month_days[month]

    if m1 != m2:
        total_days += d2
    else:
        total_days += d2 - d1 + 1

    start_index = 0 
    target_index = day_name.index(target_day)
    
    start_day_index = (start_index + total_days % 7) % 7

    full_weeks = total_days // 7
    remaining_days = total_days % 7
    
    occurrences = full_weeks
    for i in range(remaining_days):
        if (start_index + i) % 7 == target_index:
            occurrences += 1
    
    return occurrences

target_day = input()

print(count_weekday_occurrences(m1, d1, m2, d2, target_day))