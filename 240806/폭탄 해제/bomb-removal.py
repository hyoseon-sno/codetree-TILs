code,color,second=tuple(input().split())

class Bomb:
    def __init__(self,code,color,second):
        self.code=code
        self.color=color
        self.second=second

b=Bomb(code,color,int(second))

print(f"code : {b.code}")
print(f"color : {b.color}")
print(f"second : {b.second}")