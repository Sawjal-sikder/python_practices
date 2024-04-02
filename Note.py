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

n = int(input("Enter Number : "))
nRev = n[::-1]

if n==nRev:
    print("True")
else:
    print("False")



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