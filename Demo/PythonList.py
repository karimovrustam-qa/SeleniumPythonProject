
my_List = ["Tokyo", "London", "New York"]
print(my_List)
print(my_List[2])

my_List[2] = "New Delhi"
print(my_List)

for val in my_List:
    print(val)

print((len(my_List)))

my_List.append("Boston")
print(my_List)

my_List.insert(4, "Durham")
print(my_List)

my_List.remove("Tokyo")
print(my_List)
my_List.pop(1)
print(my_List)

del my_List[1]
print(my_List)

my_List.clear()
print(my_List)

fruits = ["apples", "oranges", "cherry"]
print(fruits)
fruits.reverse()
print(fruits)

my_List_2 = ["apples", 1,2,3.0]
my_List_3 = ["apples", [1,2,3], ["a","b","c"]]
print(my_List_3[1][1])
