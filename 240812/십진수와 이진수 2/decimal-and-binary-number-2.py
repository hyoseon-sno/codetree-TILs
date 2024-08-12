N=list(input())
N.reverse()
result=[]

a=0

for i in range(len(N)):
    if i==0:
        a+=1
    elif N[i]=='1':
        a+=2**i
    elif N[i]=='0':
        continue

a=a*17

print(a)

while True:
    if a<2:
        result.append(a)
        break
    else:
        x=a%2
        result.append(x)
        a=a//2

for j in result[::-1]:
    print(j,end="")