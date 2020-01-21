class BMIclac:
    def __init__(self, bmi, sex):
        self.bmi = bmi
        self.sex = sex

        self.BMItable = {"no_sex": ("FEHLER", ("Untergewicht", 0.0, 18.4), ("Normalgewicht", 18.5, 24.9),
                                    ("Übergewicht", 25.0, 29.9),
                                    ("Starkes Übergewicht(Apdipositas Grad I)", 30.0, 34.9),
                                    ("Apdipositas Grad II", 35.0, 39.9),("Adipositas Grad III", 40.0, 1000000000000.0)),
                         "male": ("FEHLER", ("Untergewicht", 0.0, 20.0), ("Normalgewicht", 20.0, 24.9),
                                  ("Übergewicht", 25.0, 29.9), ("Starkes Übergewicht(Apdipositas Grad I)", 30.0, 34.9),
                                  ("Apdipositas Grad II", 35.0, 39.9), ("Adipositas Grad III", 40.0, 10000000000000.0)),
                         "female": ("FEHLER", ("Untergewicht", 0.0, 19.0), ("Normalgewicht", 19.0, 23.9),
                                    ("Übergewicht", 24.0, 29.9),
                                    ("Starkes Übergewicht(Apdipositas Grad I)", 30.0, 34.9),
                                    ("Apdipositas Grad II", 35.0, 39.9), ("Adipositas Grad III", 40.0, 100000000000.0))}

    def set_result(self):
        counter = 1
        result = 0
        bmitable = self.BMItable["no_sex"]
        if self.sex == "male":
            bmitable = self.BMItable["male"]
        if self.sex == "female":
            bmitable = self.BMItable["female"]
        for element in bmitable[1:]:
            if self.bmi > element[1] < element[2]:
                result = counter
            counter = counter + 1
        print(bmitable[result][0])

    def set_bmi(self):
        pass


bmi = float(input("BMI: "))
sex = str(input("Sex: "))
BMI = BMIclac(bmi, sex)

BMI.set_result()
