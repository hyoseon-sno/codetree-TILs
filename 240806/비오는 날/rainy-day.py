n=int(input())
arr=[tuple(input().split()) for _ in range(n)]

class WeatherDate:
    def __init__(self,date,day,weather):
        self.date=date
        self.day=day
        self.weather=weather

a=[WeatherDate(date,day,weather) for date,day,weather in arr if weather == "Rain"]

a.sort(key=lambda x: x.date)

b=a[0]

print(f"{b.date} {b.day} {b.weather}")