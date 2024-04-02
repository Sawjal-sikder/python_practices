# Exercise 1: Print First 10 natural numbers using while loop
# n = 1
# while n < 11:
#     print(n)
#     n += 1


# Exercise 2: Print the following pattern
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

# n = 5
# for i in range(1,n+1,1):
#     for j in range(1,i+1,1):
#         print(j, end=" ")
#     print(" ")



# Exercise 3: Calculate the sum of all numbers from 1 to a given number

# number = int(input("Enter Your Number : "))
# store = 0

# for i in range(1,number+1,1):
#     store += i
# print(store)


# result = sum(range(1,number+1))
# print(result)


# Exercise 4: Write a program to print multiplication table of a given number
# For example, num = 2 so the output should be


# n =2
# for i in range(1,10,1):
#     print(n*i)



# Exercise 5: Display numbers from a list using loop
# program to display only those numbers from a list that satisfy the following conditions

# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop
# Given:
# numbers = [12, 75, 150, 180, 145, 525, 50]

# for i in numbers:
#     if i > 500:
#         break
#     elif i > 150:
#         continue
#     elif i%5 == 0:
#         print(i)


# Exercise 7: Print the following pattern
# Write a program to use for loop to print the following reverse number pattern
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

# row = 5
# k = 5
# for i in range(0,row+1,1):
#     for j in range(k-i,0,-1):
#         print(j, end=(" "))
#     print(" ")


# Exercise 8: Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]

# list1 = list1[::-1]
# for i in list1:
#     print(i)

# list1.sort(reverse=True)
# for i in list1:
#     print(i)

# lenth = len(list1)

# for i in range(lenth-1, -1,-1):
#     print(list1[i])
list1 = reversed(list1)
for i in list1:
    print(i)