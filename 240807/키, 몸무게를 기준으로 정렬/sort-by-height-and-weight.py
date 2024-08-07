n=int(input())

arr=[tuple(input().split()) for _ in range(n)]

arr.sort(key=lambda x: (int(x[1]), -int(x[2])))

for person in arr:
    print(person[0], person[1], person[2])