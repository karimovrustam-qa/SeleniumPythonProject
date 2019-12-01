def printHello():
    print("Hello")

printHello()

def printHi(name="John"):
    print("Hi,"+name)

printHi("Rustam")
printHi()

def sum(a,b,c):
    print(a+b+c)

sum(10,20,30)


def sum(a,b,c):
    print(a+b+c)

print("Enter the number:")
a = int(input())
b = int(input())
c = int(input())
sum(a,b,c)

def returnSum(a,b):
    """"this is function to calculate some of two numbers"""
    return (a+b)

x = returnSum(10,20)
print(x)