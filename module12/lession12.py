# # BMI Calculator in Python
#
# def calculate_bmi(weight, height):
#     # Calculate BMI using the formula: BMI = weight (kg) / (height (m))^2
#     height_in_meters = height / 100  # Convert height from cm to meters
#     bmi = weight / (height_in_meters ** 2)
#     return bmi
#
# def get_bmi_category(bmi):
#     # Return the BMI category based on the BMI value
#     if bmi < 18.5:
#         return "Underweight"
#     elif 18.5 <= bmi < 24.9:
#         return "Normal weight"
#     elif 25 <= bmi < 29.9:
#         return "Overweight"
#     else:
#         return "Obesity"
#
# def main():
#     print("Welcome to the BMI Calculator!")
#
#     # Get user input for weight and height
#     weight = float(input("Enter your weight in kg: "))
#     height = float(input("Enter your height in cm: "))
#
#     # Calculate BMI
#     bmi = calculate_bmi(weight, height)
#
#     # Get the BMI category
#     category = get_bmi_category(bmi)
#
#     # Print the result
#     print(f"Your BMI is: {bmi:.2f}")
#     print(f"Category: {category}")
#
#     # Provide some recommendations based on the BMI category
#     if category == "Underweight":
#         print("Recommendation: You may want to gain weight in a healthy way. Consult with a healthcare professional.")
#     elif category == "Normal weight":
#         print("Recommendation: Keep up the good work! Maintain a balanced diet and regular exercise.")
#     elif category == "Overweight":
#         print("Recommendation: Consider adopting a healthy lifestyle with proper diet and exercise.")
#     elif category == "Obesity":
#         print("Recommendation: It is recommended to consult a healthcare professional for personalized advice.")
#
# if __name__ == "__main__":
#     main()



from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self._weight = weight  # Encapsulated attribute
        self._height = height  # Encapsulated attribute

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self._weight = value
        else:
            raise ValueError("Weight must be positive")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise ValueError("Height must be positive")

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    def print_info(self):
        bmi = self.calculate_bmi()
        category = self.get_bmi_category()
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight} kg")
        print(f"Height: {self.height} m")
        print(f"BMI: {bmi:.2f}")
        print(f"Category: {category}")

class Adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 24.9 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

class Child(Person):
    def calculate_bmi(self):
        return (self.weight / (self.height ** 2)) * 1.1  # Adjustment factor

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 14:
            return "Underweight"
        elif 14 <= bmi < 18:
            return "Normal weight"
        elif 18 <= bmi < 22:
            return "Overweight"
        else:
            return "Obese"

# User input and object creation
def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    if age >= 18:
        person = Adult(name, age, weight, height)
    else:
        person = Child(name, age, weight, height)

    person.print_info()

if __name__ == "__main__":
    main()
