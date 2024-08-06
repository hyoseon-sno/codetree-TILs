name,code=tuple(input().split())

class Product:
    def __init__(self,name,code):
        self.name="codetree"
        self.code=50

p=Product(name, int(code))

print(f"product {p.code} is {p.name}")
print(f"product {code} is {name}")