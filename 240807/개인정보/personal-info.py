arr=[tuple(input().split()) for _ in range(5)]

arr.sort(key=lambda x: x[0])

print("name")
for personal in arr:
    print(personal[0], personal[1], personal[2])

arr.sort(key=lambda x: -int(x[1]))

print("")
print("height")
for personal in arr:
    print(personal[0], personal[1], personal[2])