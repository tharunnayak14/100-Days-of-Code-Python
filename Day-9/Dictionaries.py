# key value pairs

# {key : value}

dictionary = {
    "Bug": "A mistake in program",
    "Tharun": "My name"
}
print(dictionary)

# indexing using keys

print(dictionary["Bug"])
print(dictionary["Tharun"])

# add into dictionary

dictionary["Hyderabad"] = "My city"

print(dictionary)

# empty dictionary
empty_dictionary = {}

# looping through dictionary
for key in dictionary:
    print(key)
    print(dictionary[key])