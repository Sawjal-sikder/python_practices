# Strings are Arrays
x = "Hello world"
# print(x[3])
# print(x[2:5])
# print(len(x))

# y = str(input("Search : "))
# print(y in x)
# if y in x:
#     print("Yes")

# print(x[2:6])
# print(x[:6])
# print(x[6:])
# print(x[-7:-2])

# print(x.replace("H", "J"))
# print(x.split(","))



# While Loop:
    
a = 0

while a <= 10: 
    print(a)
    a+=1
a = True

if a:
    print('ok')
a = 10

if a%2 == 0: print('ok') , print('done')
year = int(input('Enter a year: '))

if year%4 == 0:
    if year%100 == 0:
        if year%400==0:
           print('Leap Year')
        else:
            print('Not Leap year')
    else:
        print('Leap Year')
else:
    print('Not Leap year')
a = 100

if a<50:
    if a>8:
        if a == 10: 
            print('ok')
        else:
            print('3rd not ok')
    else:
        print(' 2nd not ok')
else:
    print('1st not ok')