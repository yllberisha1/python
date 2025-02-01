from challenge.Person import Person

class Adult(Person):
    def calculate_nmi(self):
        return self.weghit / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_nmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal Weight"
        elif 25 <= bmi <30:
            return "Overwight"
        else:
            return "Obese"