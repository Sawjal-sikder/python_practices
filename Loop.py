#1. Iterate 0 to 10 using for loop, do the same using while loop.
i = 0
# while i <= 10:
#     print(i)
#     i += 1

# 2. Iterate 10 to 0 using for loop, do the same using while loop.
# for x in range(10,0,-1):
#     print(x)

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
x = 7
# for y in range(0, x):
#     for z in range(0, y+1):
#         print("*", end="")
#     print("")

# 4. Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #


# 5. Print the following pattern:
# i = 11
# for x in range(0,i,1):
#     print(f"{x} x {x} = {x*x}")

# 6.Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
# forlist = ['Python', 'Numpy','Pandas','Django', 'Flask']
# for x in forlist:
#     print(x)


# 7. Use for loop to iterate from 0 to 100 and print only even numbers
# for x in range(0,101,2):
#     print(x)

# 7. Use for loop to iterate from 0 to 100 and print only odd number
# for x in range(1,100,2):
#     print(x)

# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
i = 0
n = 10
for x in range(1, n+1, 1):
    i += x
print(i)