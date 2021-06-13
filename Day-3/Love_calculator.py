print("Welcome to Love Calculator")
# e.g.
#
# `name1 = "Angela Yu"`
#
# `name2 = "Jack Bauer"`
#
# T occurs 0 times
#
# R occurs 1 time
#
# U occurs 2 times
#
# E occurs 2 times
#
# Total = 5
#
# L occurs 1 time
#
# O occurs 0 times
#
# V occurs 0 times
#
# E occurs 2 times
#
# Total = 3
#
# Love Score = 53
#
# Print: "Your score is 53."
name1 = input("What is your name\n")
name2 = input("What is your crush name\n")

name1 = name1.lower()
name2 = name2.lower()

true = 0
love = 0

true += name1.count('t')
true += name1.count('r')
true += name1.count('u')
true += name1.count('e')

true += name2.count('t')
true += name2.count('r')
true += name2.count('u')
true += name2.count('e')

love += name1.count('l')
love += name1.count('o')
love += name1.count('v')
love += name1.count('e')

love += name2.count('l')
love += name2.count('o')
love += name2.count('v')
love += name2.count('e')

love_score = true * 10 + love

# For Love Scores **less than 10** or **greater than 90**, the message should be:
#
# `"Your score is **x**, you go together like coke and mentos."`
#
# For Love Scores **between 40** and **50**, the message should be:
#
# `"Your score is **y**, you are alright together."`
#
# Otherwise, the message will just be their score. e.g.:
#
# `"Your score is **z**."`

if love_score <= 10 or love_score >= 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif (love_score <= 50) and (love_score >= 40):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")