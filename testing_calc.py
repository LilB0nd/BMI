class BMIclac:
    def __init__(self, bmi):
        self.bmi = bmi
        self.sex = "male"
        self.BMItable = {"no_sex": ("FEHLER", ("Untergewicht", 0, 18.4), ("Normalgewicht", 18.5, 24.9),
                                    ("Übergewicht", 25, 29.9), ("Starkes Übergewicht(Apdipositas Grad I)", 30, 34.9),
                                    ("Apdipositas Grad II", 35, 39.9),("Adipositas Grad III", 40, 0)),
                         "male": ("FEHLER", ("Untergewicht", 0, 20), ("Normalgewicht", 20, 24,9),
                                  ("Übergewicht", 25, 29.9), ("Starkes Übergewicht(Apdipositas Grad I)", 30, 34.9),
                                  ("Apdipositas Grad II", 35, 39.9), ("Adipositas Grad III", 40, 0)),
                         "female": ("FEHLER", ("Untergewicht", 0, 19), ("Normalgewicht", 19, 23,9),
                                    ("Übergewicht", 24, 29.9),
                                    ("Starkes Übergewicht(Apdipositas Grad I)", 30, 34.9),
                                    ("Apdipositas Grad II", 35, 39.9), ("Adipositas Grad III", 40, 0))}

    def set_result(self):
        counter = 1
        result = 0
        if self.sex == "male": bmitable = self.BMItable["male"]
        if self.sex == "female": bmitable = self.BMItable["female"]
        if self.sex == "no_sex": bmitable = self.BMItable["no_sex"]
        for element in bmitable[1:]:
            counter = counter + 1
            if self.bmi > element[1] < element[2]:
                result = counter
        print(bmitable[result][0])


bmi = float(input("BMI:"))
BMI = BMIclac(bmi)

BMI.set_result()
