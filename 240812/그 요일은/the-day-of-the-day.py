def count_weekday_occurrences(m1, d1, m2, d2, target_day):
    month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_name = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    target_index = day_name.index(target_day)
    
    occurrences = 0

    current_day_of_week = 0 
    total_days = 0

    for month in range(1, m1):
        total_days += month_days[month]
    
    total_days += d1 - 1
    
    current_day_of_week = (current_day_of_week + total_days) % 7
    
    for month in range(m1, m2 + 1):
        start_day = d1 if month == m1 else 1
        end_day = d2 if month == m2 else month_days[month]
        
        for day in range(start_day, end_day + 1):
            if current_day_of_week == target_index:
                occurrences += 1
            current_day_of_week = (current_day_of_week + 1) % 7

    return occurrences

m1, d1, m2, d2 = map(int, input().split())
target_day = input()

print(count_weekday_occurrences(m1, d1, m2, d2, target_day))