N,B=map(int,input().split())
arr=[]

while True:
    if N<B:
        arr.append(N)
        break
    else:
        x=N%B
        arr.append(x)
        N=N//B

for i in arr[::-1]:
    print(i,end="")