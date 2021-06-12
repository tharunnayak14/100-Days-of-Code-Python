# add digits of a number
var = input("Enter a number\n")

ans = 0
for i in range(len(var)):
    ans = ans + int(var[i])

print(ans)