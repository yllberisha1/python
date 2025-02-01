from challenge.Person import Person

class Adult(Person):
    def calculate_nmi(self):
        return self.weghit / (self.height ** 2) * 1.3

    def get_bmi_category(self):
        bmi = self.calculate_nmi()
        if bmi < 14:
            return "Underweight"
        elif 14 <= bmi < 18:
            return "Normal Weight"
        elif 18 <= bmi <24:
            return "Overwight"
        else:
            return "Obese"