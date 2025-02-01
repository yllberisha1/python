from abc import ABC

class Person(ABC):
    def __init__(self, name,age,weight,height):
        self.name= name
        self.age = age
        self.weight= weight
        self.height = height


    @property
    def weight(self):
        return self.weight

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError("weight cannot be negative")
        self.weight = value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("height cannot be negative")
        self.height = value

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}, Height: {self.height}")

