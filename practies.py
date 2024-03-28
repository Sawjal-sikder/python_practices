# # Variable
# MyName = "md sawjal Sikder"
# print(MyName)
# # swap
# a = 5
# b = 10
# print(a,b)
# a,b = b,a
# print(a,b)
# # Multiple Variable
# a,b,c = "Md", "Sawjal", "sikder"
# print(a)

# # One value to multiple variable
# a=b=c = "Md Sawjal Sikder"
# print(c)

# # Unpack collection
# fruits = "Apple", "Orange", "Banana"
# a,b,c = fruits
# print(a)

# # f string
# Name = "Md Sawjal Sikder"
# Age = 30
# print(f"Hello, My name is {Name} and age is {Age} years old.")

# # Data type 
# print(type(Name))
# print(float(Age))

# # Multiline String
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)
# print(Name[3:9])

# # Looping Through a String
# for x in Name:
#     print(x)
# print(len(Name))
# print("Md" in Name)

# if "Md" in Name:
#     print(f"Yes, Md are availavle in {Name}")

# print(Name[::-1])
# print(Name.upper())
# print(Name.lower())
# print(Name.replace("Sawjal", "Sajal"))
# print(Name.split(" "))

# a = "Hello"
# b = "World"
# c = a+b
# print(c)
# print(a," ", b)
# print(f"{a} {b}")

# print(Name.capitalize())
# c = Name.count("Md Sawjal Sikder")
# print(c)

# List in python
# mylist = ["apple", "banana", "cherry"]
# listi = ("apple", "banana", "cherry")
# print(mylist)
# print(len(mylist))
# print(type(mylist))
# print(list(listi))

# print(mylist[2])
# print(mylist[:2])
# print(mylist[1:])
# print(mylist[::-1])

# if "apple" in mylist:
#     print(f"{mylist[0]} in the list")

# mylist[1] = "Orange"
# print(mylist)

# mylist[1:3] = ["blackcurrant", "watermelon"]
# print(mylist)

# mylist.insert(2, "Orange")
# print(mylist)

# mylist.append("Banana")
# print(mylist)

# tropical = ["mango", "pineapple", "papaya"]
# mylist.extend(tropical)
# print(mylist)

# mylist.remove(["Banana"])
# print(mylist)

# mylist.pop(1)
# print(mylist)

# mylist.pop()
# print(mylist)

# del mylist[-1]
# print(mylist)


# i = int(input("Enter your Nunnber : "))

# while i <= 10:
#     print(i)
#     i += 1

# while i < 10:
#     print(i)
#     i += 1
#     if i == 5:
#         break

# while i < 10:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# while i < 10:
#     print(i)
#     i += 1
# else:
#     print("The End")


# while i < 10:
#     print(i)
#     i += 1 
#     if i == 4:
#         break


# while i < 10:
#     i += 1
#     if i == 5:
#         continue
#     print(i)
# else:
#     print("End the while loop")

fruits = ["apple", "banana", "cherry"]

# for x in fruits:
#     print(x)


# for x in "Md Sawjal Sikder":
#     print(x)

# for x in fruits:
#     print(x)
#     if x == "banana":
#         break


# for x in fruits:
#     if x == "banana":
#         continue
#     print(x)


# for x in range(1,11,1):
#     print(f"5 x {x} = {x*5}")