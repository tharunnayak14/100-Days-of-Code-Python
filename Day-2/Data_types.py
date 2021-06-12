# strings

# print first char
print("hello"[0])
print('hello'[4])

# concat strings
print("123" + "345")
# add numbers
print(123 + 345)

# 123_456_789 same as 123456789

# float

var = 3.14

# boolean

var1 = True
var2 = False

print(type(var))
print(type(var1))


# math operators

print(3+5)
print(2-4)
print(3*4)
# prints float
print(2/3)
# exponent 5^3
print(5**3)
# floor division (int)
print(5//3)

# order of priority
# ()
# **
# * /
# + -

print(3*3+3/3-3)  # ((3*3)+ (3/3) - 3) --> (9+1-3) --> 7

# round(no, no_of_digits)
print(round(8/3, 6))



# f-string

score = 1
height = 1.8
print(f"your score is {score}, your height is {height}")
