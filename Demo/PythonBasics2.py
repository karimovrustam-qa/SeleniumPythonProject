
if 5 > 3:
    print("5 is greater then 3")

print("Enter the number:")
num = int (input())
if num > 0:
    print("This is positive num")
elif num == 0:
    print("Num equals 0 ")
else:
    print("This is negative num")

num = [1,2,3,4,5]

for val in num:
    print(val)

num = [1,2,3,4,5]
sum = 5
for ammount in num:
    sum=sum+ammount
print("Total is",sum)

fruits = ["apple", "orange", "mango"]
for val in fruits:
    print(val)
else:
    print("No fruits left")

num = 6
sum = 0
i = 1

while i<num:
    sum=sum+i
    i=i+2
print("Total is:", sum)

print("Enter the number:")
num = int(input())
sum = 0
i = 1

while i<num:
    sum=sum+i
    i=i+1
print("Total is:", sum)