A = input()

def func01(string):
    leng = len(string)
    for i in range(leng):
        if string[i] != string[0]:
            return True
    
    return False


if func01(A):
    print("Yes")
else:
    print("No")