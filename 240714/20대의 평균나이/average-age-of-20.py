a=0
b=0
count=0

while True:
    n=int(input())

    if n >29:
        break;
    if n<30:
        count+=1
        a+=n
b=a/count
print(f"{b:.2f}")