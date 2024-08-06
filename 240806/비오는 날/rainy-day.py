class WeatherData:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())
weather_data = [input().split() for _ in range(n)]

rainy_days = [WeatherData(date, day, weather) for date, day, weather in weather_data if weather == "Rain"]

rainy_days.sort(key=lambda x: x.date)

earliest_rainy_day = rainy_days[0]
print(f"{earliest_rainy_day.date} {earliest_rainy_day.day} {earliest_rainy_day.weather}")