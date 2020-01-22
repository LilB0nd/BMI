class BMIclac:
    def __init__(self, sex, weight, size):
        self.sex = sex
        self.weight = weight
        self.size = size
        self.BMItable = {"no_sex": (("FEHLER", None), ("Untergewicht", 0.0, 18.4), ("Normalgewicht", 18.5, 24.9),
                                    ("Übergewicht", 25.0, 29.9),
                                    ("Starkes Übergewicht(Apdipositas Grad I)", 30.0, 34.9),
                                    ("Apdipositas Grad II", 35.0, 39.9),("Adipositas Grad III", 40.0, 200.0)),
                         "male": (("FEHLER", None), ("Untergewicht", 0.0, 20.0), ("Normalgewicht", 20.0, 24.9),
                                  ("Übergewicht", 25.0, 29.9), ("Starkes Übergewicht(Apdipositas Grad I)", 30.0, 34.9),
                                  ("Apdipositas Grad II", 35.0, 39.9), ("Adipositas Grad III", 40.0, 200.0)),
                         "female": (("FEHLER", None), ("Untergewicht", 0.0, 19.0), ("Normalgewicht", 19.0, 23.9),
                                    ("Übergewicht", 24.0, 29.9),
                                    ("Starkes Übergewicht(Apdipositas Grad I)", 30.0, 34.9),
                                    ("Apdipositas Grad II", 35.0, 39.9), ("Adipositas Grad III", 40.0, 200.0))}

    def set_result(self):
        counter = 1
        result = 0
        bmitable = self.BMItable["no_sex"]
        if self.sex == "male":
            bmitable = self.BMItable["male"]
        if self.sex == "female":
            bmitable = self.BMItable["female"]
        for element in bmitable[1:]:
            if self.bmi > element[1] and self.bmi < element[2]:
                result = counter
            counter = counter + 1
        print(bmitable[result][0])

    def set_bmi(self):
        self.bmi = round(self.weight/(self.size**2), 1)
        print(self.bmi)


sex = str(input("Sex: "))
weight = float(input("Weight in kg: "))
size = ((float(input("Size in cm: "))) / 100)

BMI = BMIclac(sex, weight, size)
BMI.set_bmi()
BMI.set_result()
