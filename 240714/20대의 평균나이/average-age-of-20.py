a = 0
count = 0

try:
    while True:
        n = int(input())
        if n > 29:
            break
        if n < 30:
            count += 1
            a += n
except EOFError:
    pass

if count > 0:
    b = a / count
    print(f"{b:.2f}")
else:
    print("No valid input received")