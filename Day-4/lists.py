# list data structure
# storing multiple values in a single variable

fruits = ['apple', 'banana', 'mango']
print(fruits)

# indexing in lists (0-indexing)
print(fruits[0])
print(fruits[1])
print(fruits[2])

# negative indexing
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])

# add in to list
fruits.append("cherry")
# add multiple items into list
fruits.extend(["guava", "papaya", "blueberry"])
# slicing in lists

# get everything from the list
print(fruits[:])
# get everything from index 0 to index 1 (2 not included)
print(fruits[0:2])