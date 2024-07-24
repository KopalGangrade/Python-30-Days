# s= "my name is kopal"

# d="".join(s.split())
# print(d)

n=int(input())
d=str(n)
m=len(d)
sum=0
for i in d:
    sum+=int(i) ** m
if (sum==n):
    print("yes")
else:
    print("No")

# n = int(input("Enter a number: "))
# d = str(n)
# m = len(d)
# armstrong_sum = 0

# for digit in d:
#     armstrong_sum += int(digit) ** m

# if armstrong_sum == n:
#     print("Yes")
# else:
#     print("No")



