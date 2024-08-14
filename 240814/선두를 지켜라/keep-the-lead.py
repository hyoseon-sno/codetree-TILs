N,M=map(int,input().split())
narr=[]
marr=[]
narr.append(0)
marr.append(0)
x=0
y=0

for _ in range(N):
    n_v, n_t=map(int,input().split())
    for i in range(n_t):
        narr.append(x+n_v)
        x=x+n_v

for _ in range(M):
    m_v, m_t=map(int,input().split())
    for j in range(m_t):
        marr.append(y+m_v)
        y=y+m_v

m=max(len(narr),len(marr))      
rarr=[]

for z in range(m):
    if narr[z]>marr[z]:
        rarr.append("n")
    elif narr[z]<marr[z]:
        rarr.append("m")

result=0

for r in range(1,len(rarr)):
    if rarr[r-1]!=rarr[r]:
        result+=1

print(result)