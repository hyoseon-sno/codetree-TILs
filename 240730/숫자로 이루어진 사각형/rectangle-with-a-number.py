n=int(input())
j=1

for _ in range(n):
    for _ in range(n):
        print(j, end=" ")
        if j != 10:
            j+=1
        if j == 10:
            j=1
    print()