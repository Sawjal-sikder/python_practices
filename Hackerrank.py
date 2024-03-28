# n = int(input("Enter Your Number : "))
# for i in range(1, n+1):
#     print(i, end="")
# print("")


x = int(1)
y = int(1)
z = int(2)
n = int(3)
store = []
for a in range(x+1):
        for b in range(y+1):
            for c in range(z+1):
                  if a+b+c == n:
                        continue
                  store.append([a,b,c])
print(store) 


