a, o, c = input().split()
a = int(a)
c = int(c)

def func01(a, o, c):
    x = a + c
    print(f"{a} {o} {c} = {x}")

def func02(a, o, c):
    x = a - c
    print(f"{a} {o} {c} = {x}")

def func03(a, o, c):
    x = a // c
    print(f"{a} {o} {c} = {x}")

def func04(a, o, c):
    x = a * c
    print(f"{a} {o} {c} = {x}")

if o == '+':
    func01(a, o, c)
elif o == '-':
    func02(a, o, c)
elif o == '/':
    func03(a, o, c)
elif o == '*':
    func04(a, o, c)
else:
    print("False")