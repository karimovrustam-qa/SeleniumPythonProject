class MyClass:
    name = "White nights"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sum(self,a,b):
        print(a+b)

x = MyClass("John", 40)
print (x.name)
x.sum(4,5)
del x.name
print(x.age)