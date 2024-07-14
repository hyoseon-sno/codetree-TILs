n=int(input())
count=0

for i in range(n):
    student=list(map(int,input().split()))
    total,score=0,0
    for i in range(4):
        total+=student[i]
        score=total/4

    if score >= 60:
        print("pass")
        count+=1
    else :
        print("fail")

print(count)