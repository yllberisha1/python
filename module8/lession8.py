#def  calculate_area(width, length):
#    return width * length

#def calculate_perimeter(width, length):
#  return 2 * (width + length)

#length = 5
#width = 6

#area = calculate_area(width, length)
#perimeter = calculate_perimeter(width, length)


#print(f"area, {area}")
#print(f"perimeter, {perimeter}")



class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

my_rectangle = Rectangle(5, 3)

area = my_rectangle.calculate_area()
perimeter = my_rectangle.calculate_perimeter()

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, I am {self.name},and I am {self.age} years old ")


persion1 = Person("Ylli", 17)
persion2= Person("Camavinga", 23)

persion1.greet()
persion2.greet()
