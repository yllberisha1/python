from lesson2.lesson2 import person


class BMIApp:
    def __init__(self):
        self.people= []
        def add_person(self, person):
            self.people.append(person)

        def collect_user_data(self):
            name - input("enter name:")
            age = int(input("enter age:"))
            weight = float(input("enter weight:"))
            height = float(input("enter height:"))

            if age >=18:
                person = Adult(name, age, weight, height)
            else:
                person = Child(name, age, weight, height)

            self.add_person(person)

        def print_results(self):
            for person in self.people:
                person.print_info()

        def run(self):
            while True:
                self.collet_user_data()
                const=input("Do you what to add another person? (yes/no):"), script(),loer()
