total = 0

for number in range(1,11):
    if number % 2 == 0:
        total += number
print("Shuma e numrave qift prej 1 deri ne 10 eshte:", total)

def greet():
    print("Hello World")

greet()

def greet_person(name):
    print("Hello", name)

greet_person("Filan")

#result = add(3,8)
#print("3 + 7=", result)

greeting = "Hello"

def greet(name):
    message = f"{greeting}, {name}!"
    print(message)
greet("Michael")
print(greeting)



def greet_person(name, greeting="Hello"):
    message = f"{greeting}, {name}!"
    return message

default_greeting = greet_person("Rian")
custom_greeting = greet_person("Eris", "Hi")
print(default_greeting)
print(custom_greeting)