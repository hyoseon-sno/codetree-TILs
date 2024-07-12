room=2
room_count=0
stair=3
stair_count=0
bath=12
bath_count=0

n=int(input())

for i in range(0,n):
    if i>=12 and i % 12 == 0 :
        bath_count +=1
    elif i>=3 and i % 3 == 0 :
        stair_count +=1
    elif i>=2 and i % 2 == 0 :
        room_count +=1
    
print(room_count,stair_count,bath_count)