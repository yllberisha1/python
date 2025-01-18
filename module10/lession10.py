from abc import ABC, abstractmethod


class shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(shape):
    def init(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Square(shape):
    def init(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


circle = Circle(7)
square = Square(10)

print(circle.area())
print(square.area())


class Printable(ABC): 1 usage
@abstractmethod  def print_info(self):
pass
class Book(Printable): 1 usage  def -_init__(self, title, author):
self. title = title
self.author = author
def print_info(self): 1 usage
print(f"Book: (self.title} by (self.author]")
book = Book( title: "Fugia e se tashmes", author: "Ismail Kadare")
book. print_info()














#     def __init__(self, age, name):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#          self.__name = name
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):
#         self.__age = age
#
#
#
# student1 = Student(17, "Yll")
# print("name:", student1.get_name())
# student1.set_name("Camavinga")
# print("updated name:", student1.get_name())
#
# print("age",student1.get_age())
# student1.set_age(18)
# print("updated age:", student1.get_age())


