arr = list(map(float, input().split()))  
result = 0

for i in range(8):
    result += arr[i]

result = result / 8

print(f"{result:.1f}")