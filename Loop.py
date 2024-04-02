# 1. Write a Python program to schedule the tasks in such a way that the total penalty for missing deadlines is minimized. Your program should output the optimal order of tasks and the total penalty incurred.
# Input:
# A list of tasks, where each task is represented as a tuple (deadline, penalty). The deadline is an integer representing the number of days until the task must be completed, and the penalty is an integer representing the penalty for missing the deadline.
# Output:
# The optimal order of tasks to minimize the total penalty.
# The total penalty incurred.
# Example:
# Input:
# tasks = [(3, 100), (1, 300), (2, 200)]
# Output:
# Optimal order of tasks: [(1, 300), (2, 200), (3, 100)]
# Total penalty incurred: 600
# Note: In this example, completing the tasks in the order (1, 300), (2, 200), (3, 100) incurs a total penalty of 600, which is the minimum penalty possible for the given tasks.
    





# 2. Given an integer x, return true if x is a palindrome, and false otherwise.




# 3. Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
 
# Example 1:Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.





# 4.Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
 
# Example 1:Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:Input: n = 1
# Output: ["()"]

 
# Constraints:
# 1 <= n <= 8



# 5.Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).
 
# Example 1:Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.

# Example 3:Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

 
# Constraints:
# 0 <= s.length, p.length <= 2000
# s contains only lowercase English letters.
# p contains only lowercase English letters, '?' or '*'.




# 6.3The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.
 
# Example 1:Input: n = 3, k = 3
# Output: "213"

# Example 2:Input: n = 4, k = 9
# Output: "2314"

# Example 3:Input: n = 3, k = 1
# Output: "123"

 
# Constraints:
# 1 <= n <= 9
# 1 <= k <= n!
=======
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
