# Q8. Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria:

# 1. First 100 units 	No Charge
# 2. Next 100 unites 	Rs 5 per unit
# 3. after 200 units 	Rs 10 per unit
# (for example if input unit is 350 than total bill amount is Rs 2000)

# unit = int(input("Enter unit"))
# bill = 0

# if unit <= 100:
#     print("No Charge")
# elif unit > 100 and unit <=200:
#     print((unit-100)*5)
# elif unit > 200:
#     print(500+(unit-200)*10)
# else:
#     print("Error")



# part 2
# Q1.Write a program to accept percentage from the user and display the grade according to the following criteria:

# marks			    Grade
# >90			    A
# >80 and <=90		B
# >=60 and <=80		c
# below 60		    d

# marks = int(input("Enter Marks :"))

# if marks > 90:
#     print("Grade is : A")
# elif marks > 80 and marks <= 90:
#     print("Grade is : B")
# elif marks >= 60 and marks <= 80:
#     print("Grade is : C")
# elif marks < 60 :
#     print("Grade is : D")
# else:
#     print("Failed")


# Q2.Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria:

# cost price (in Rs)	Tax
# >100000			    15%
# >50000 and <=100000	10%
# <=50000			    5%

# price = float(input("Enter your Bike price : "))

# if price > 100000:
#     print(price*0.15)
# elif price > 50000 and price<= 100000:
#     print(price*0.10)
# elif price < 50000 :
#     print(price*0.05)
# else:
#     print("error")





# Q4. Write a program to accept a number from 1 to 7 and display the name of the day like 1 for sunday. 
# 2 for monday and so on.

# number = int(input("Enter a number from 1 to 7 : "))

# if number == 1:
#     print("Sunday")
# elif number == 2:
#     print("Monday")
# elif number == 3:
#     print("Tuesday")
# elif number == 4:
#     print("Wednesday")
# elif number == 5:
#     print("Thusday")
# elif number == 6:
#     print("Friday")
# elif number == 7:
#     print("Saturday")
# else:
#     print("Error")


# Q5. Write a program to accept a number from 1 to 12 and display of the month and days in that month like
# 1 for january and number of days 31 and so on