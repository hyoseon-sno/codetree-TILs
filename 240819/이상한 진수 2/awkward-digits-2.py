a = input()

max_value = 0

for i in range(len(a)):
    arr = list(a)
    
    if arr[i] == '1':
        arr[i] = '0'
    elif arr[i] == '0':
        arr[i] = '1'
    
    new_value = int(''.join(arr), 2)
    max_value = max(max_value, new_value)

print(max_value)