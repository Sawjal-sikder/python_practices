# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is equal to or lower than 1000. 
# Otherwise, return their sum.

# def multi1(number1,number2):
#     into = number1 * number2
#     sum = number1 + number2
#     if into <= 1000:
#         return into
#     else:
#         return sum

# fristProblem = multi1(20,30)
# print(fristProblem)
# seceondProblem = multi1(40,30)
# print(seceondProblem)


# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

# previousNumber = 0

# for i in range(0,10,1):
#     print(f'Current Number is : {i} Previous Number is : {previousNumber} Total Number is : {previousNumber+i}')
#     previousNumber = i


# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

# pyVariable = "pynative"
# lenthVariable = len(pyVariable)

# for i in range(0,lenthVariable - 1, 2):
#     print(pyVariable[i])



# Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.
# For example:
# remove_chars("pynative", 4) so output must be tive. Here, we need to remove the first four characters from a string.
# remove_chars("pynative", 2) so output must be native. Here, we need to remove the first two characters from a string.

# def remove_chars(name, n):
#     remove_text = name[n:]
#     return remove_text
# Output1 =  remove_chars("pynative", 4)
# print(f'Out of 4 character is : {Output1}')
# Output2 =  remove_chars("pynative", 2)
# print(f'Out of 2 character is : {Output2}')



# Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

# def myList(ListArgument):
#     firstNumber = ListArgument[0]
#     lastNumber = ListArgument[-1]
#     if firstNumber == lastNumber:
#         return True
#     else:
#         return False    

# numbers_x = [10, 20, 30, 40, 10]
# print(myList(numbers_x))
# numbers_y = [75, 65, 35, 75, 30]
# print(myList(numbers_y))



# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5
# Expected Output:
# Given list is  [10, 20, 33, 46, 55]
# Divisible by 5
# 10
# 20
# 55

# mylist = [10, 20, 33, 46, 55]

# for i in mylist:
#     if i%5 == 0:
#         print(i)


# x = "python"
# for i in range(len(x)):
#     print(x[i])



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
a = str(input("Enter Your Search : "))

for x in fruits:
  if a in x:
    newlist.append(x)

print(newlist)

