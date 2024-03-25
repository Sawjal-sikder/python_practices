# Variable
MyName = "md sawjal Sikder"
print(MyName)
# swap
a = 5
b = 10
print(a,b)
a,b = b,a
print(a,b)
# Multiple Variable
a,b,c = "Md", "Sawjal", "sikder"
print(a)

# One value to multiple variable
a=b=c = "Md Sawjal Sikder"
print(c)

# Unpack collection
fruits = "Apple", "Orange", "Banana"
a,b,c = fruits
print(a)

# f string
Name = "Md Sawjal Sikder"
Age = 30
print(f"Hello, My name is {Name} and age is {Age} years old.")

# Data type 
print(type(Name))
print(float(Age))

# Multiline String
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print(Name[3:9])

# Looping Through a String
for x in Name:
    print(x)
print(len(Name))
print("Md" in Name)

if "Md" in Name:
    print(f"Yes, Md are availavle in {Name}")

print(Name[::-1])
print(Name.upper())
print(Name.lower())
print(Name.replace("Sawjal", "Sajal"))
print(Name.split(" "))

a = "Hello"
b = "World"
c = a+b
print(c)
print(a," ", b)
print(f"{a} {b}")

print(Name.capitalize())
c = Name.count("Md Sawjal Sikder")
print(c)

