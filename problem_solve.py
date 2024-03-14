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

# month = int(input("Enter a number from 1 to 12 : "))

# if month == 1:
#     print("January is 31 days")
# elif month == 2:
#     print("February is 28 days")
# elif month == 3:
#     print("March is 31 days")
# elif month == 4:
#     print("April is 30 days")
# elif month == 5:
#     print("May is 31 days")
# elif month == 6:
#     print("June is 30 days")
# elif month == 7:
#     print("July is 31 days")
# elif month == 8:
#     print("August is 31 days")
# elif month == 9:
#     print("September is 30 days")
# elif month == 10:
#     print("October is 31 days")
# elif month == 11:
#     print("November is 30 days")
# elif month == 12:
#     print("December is 31 days")
# else:
#     print("Error")

# Q9. Accept any city from the user and display monument of that city.

# 	city		Monument
# 	Delhi		Red Fort
# 	Agra		Taj Mahal
# 	Jaipu		Jal Mahal

# city = str(input("Enter City Name : "))

# if city == "Delhi":
#     print("Monument is : Red Fort")
# elif city == "Agra":
#     print("Monument is : Taj Mahal")
# elif city == "Jaipu":
#     print("Monument is : Jal Mahal")
# else:
#     print("Error")

# A company decided to give bonus to employee according to following criteria:
# Time period of service	Bonus
# More than 10 years	10%
# >=6 and <=10 years 	8%
# less than 6 years 	5%
# ask user for their salary and years of service and print the net bonus amount

# Salary = float(input("Enter Salary Here : "))
# S_Year = int(input("Enter Service Year Here : "))

# if S_Year > 10:
#     print(Salary*0.10)
# elif S_Year >= 6 and S_Year <= 10:
#     print(Salary*0.08)
# elif S_Year < 6 :
#     print(Salary*0.05)
# else:
#     print("error")


# Accept the marked price from the user and clculate the net amount as (Marketd price - discount) to pay according to following criteria:

# Maked Price		Discount
# >10000			20%
# >7000 and <=10000	15%
# <=7000			10%

# MarketPrice = float(input("Enter Market Price Here : "))
# TotalAmount = 0
# DiscountAmout = 0
# if MarketPrice > 10000:
#     DiscountAmout = MarketPrice*0.20
# elif MarketPrice > 7000 and MarketPrice <= 10000:
#     DiscountAmout = MarketPrice*0.15
# elif MarketPrice <= 7000:
#     DiscountAmout = MarketPrice*0.10
# TotalAmount = MarketPrice-DiscountAmout
# print("Net Payable Amount", TotalAmount)

# Write a program to accept Percentage and display the catagory according to the following criteria:

# Percentage		Catagory
# < 40			Failed
# >=40 & <55		Fair
# >=55 & <65		Good
# >=65 			Excellent


# Percentange = int(input("Enter Percentange Here : "))
# display = ""
# if Percentange < 40:
#     display = "Faield"
# elif Percentange >= 40 and Percentange < 55:
#     display = "Fair"
# elif Percentange >= 55 and Percentange < 65:
#     display = "Good"
# elif Percentange >= 65:
#     display = "Excellent"
# else:
#     display = "Error"
# print(display)
