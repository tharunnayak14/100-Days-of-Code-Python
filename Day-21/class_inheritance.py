# inheritance, inherit from a parent class

# parent class
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


# fish is a child class inherited from the animal parent class
class Fish(Animal):
    def __init__(self):
        # trigger call to the super class (Animal)
        super().__init__()

    def breathe(self):
        # calling breathe from the super class
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.breathe()
nemo.swim()
