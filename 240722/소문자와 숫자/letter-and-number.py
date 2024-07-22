input_string = input().strip()

result = []

for char in input_string:
    if char.islower() or char.isdigit():
        result.append(char)
    elif char.isupper():
        result.append(char.lower())

print(''.join(result))