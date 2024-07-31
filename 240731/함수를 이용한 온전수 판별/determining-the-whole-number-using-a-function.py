a,b=map(int,input().split())
count=0

def func01(i):
    if i%2==0:
        return True
    else:
        return False

def func02(i):
    if i%10==5:
        return True
    else:
        return False

def func03(i):
    if i%3==0 and i%9!=0:
        return True
    else:
        return False


for i in range(a,b+1):
    if func01(i)==False and func02(i)==False and func03(i)==False:
        count +=1

print(count)