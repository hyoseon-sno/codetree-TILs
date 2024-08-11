a,b,c=map(int,input().split())

day=(a-11) * 24* 60
day_a=60*b+c

day_b=11*60+11

if b<11:
    print("-1")
else:
    print(day+day_a-day_b)