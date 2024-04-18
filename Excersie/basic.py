x = str(input("Enter your change items : "))
n = str(input("Enter your Change Value: "))

fruits = ["apple", "banana", "cherry"]
fIndex = fruits.index(x)

fruits[fIndex] = n
print(fruits)