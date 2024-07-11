counta=0
countb=0

for _ in range(10):
    a=int(input())
    if a%3==0:
        counta=counta+1
    if a%5==0:
        countb=countb+1

print(counta,countb)