a = int(input("Enter 1st number"))
b = input("Enter Oparator")
c = int(input("Enter 2nd number"))

if b == "+":
    print(a + c)
elif b == "-":
    print(a - c)
elif b == "*":
    print(a * c)
elif b == "/":
    print(a / c)
else:
    print("Error")  