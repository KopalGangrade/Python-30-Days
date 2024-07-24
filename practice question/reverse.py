# n=int(input("enter"))

# add=""
# while n>0:
#     d=n%10 # 230
#     add = str(d)+add
#     n=n//10
#     print(d)

# -------------string---------------------

# n = input("Enter a number: ") #kopal

# add=""
# i=-1
# b=len(n)
# while b>0:
#     add+=n[i]
#     i-=1
#     b -= 1
# print(add)


# string = input("Enter a string: ")
# reverse_string = ""
# index = len(string) - 1
# print(len(string))
# print(index)

# while index >= 0:
#     reverse_string += string[index]
#     index -= 1

# print(reverse_string)

# ========using slice =================================

# string = "Python Programming"
# print(string[::-1])

# > gnimmargorP nohtyP

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 9)) # error