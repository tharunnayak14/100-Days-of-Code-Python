# class User:
#     pass
#
#
# # object
# user_1 = User()
#
# print(user_1)
#
# user_1.id = 100
# user_1.name = "Tharun"
#
# print(user_1.name)


# we can use a constructor to initialise the attributes

class User:
    # self, user_id, username  are attributes
    # init function is the constructor
    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username
        self.followers = 0


# object
user_1 = User(420, "Tharun")

# print(user_1)
print(user_1.name)



class Car:
    def __init__(self, seats, name):
        # runs everytime we initialise the object
        self.name = name
        self.seats = seats
        print(f"New {self.name} car created")
        
    # methods
    # method always has a self parameter
    def enter_race_mode(self, name):
        print(f"{name} Entered race mode")
        self.seats = 2


BMW = Car(5, "BMW")
print(BMW.seats)
BMW.enter_race_mode("BMW")
print(BMW.seats)
AUDI = Car(7, "AUDI")
print(AUDI.seats)
