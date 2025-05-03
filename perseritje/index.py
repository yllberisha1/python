class Person:
    def __init__(self, name):
     self.name = name
    def greet (self):
        print(f"Hi, Im {self.name}")


p1 = Person ("Ylli")

p1.greet()

class rectangle:
    def __init__(self, width , length):
        self.width = width
        self.length = length
    def area(self):
        return self.length * self.width

r1 = rectangle (5 , 10)

print(r1.area())

class pet:
    def __init__(self, name , age ,species, breed, color):
        self.name = name
        self.age = age
        self.species = species
        self.breed = breed
        self.color = color
    def make_sound(self):
        print(f"name of the pet is {self.name}")

pe1 = pet ("murki")






