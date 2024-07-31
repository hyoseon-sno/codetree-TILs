def dyear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def date(year, month, day):
    days_in_month = [31, 29 if dyear(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 or month > 12:
        return False
    if day < 1 or day > days_in_month[month - 1]:
        return False
    return True

def season(month):
    if 3 <= month <= 5:
        return "Spring"
    elif 6 <= month <= 8:
        return "Summer"
    elif 9 <= month <= 11:
        return "Fall"
    else:
        return "Winter"

def func01(Y, M, D):
    if date(Y, M, D):
        print(season(M))
    else:
        print(-1)

Y, M, D = map(int, input().split())
func01(Y, M, D)