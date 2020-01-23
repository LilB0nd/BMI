class BMIcalculation:
    def __init__(self, sex, weight, size, age):
        self.sex = sex
        self.weight = weight
        self.size = size
        self.age = age
        self.BMI_table = {"no_sex": (("FEHLER", None), ("Untergewicht", 0.0, 18.4), ("Normalgewicht", 18.5, 24.9),
                                     ("Übergewicht", 25.0, 29.9),
                                     ("Starkes Übergewicht(Apdipositas Grad I)", 30.0, 34.9),
                                     ("Apdipositas Grad II", 35.0, 39.9), ("Adipositas Grad III", 40.0, 1000.0)),
                         "male": (("FEHLER", None), ("Untergewicht", 0.0, 20.0), ("Normalgewicht", 20.0, 24.9),
                                  ("Übergewicht", 25.0, 29.9), ("Starkes Übergewicht(Apdipositas Grad I)", 30.0, 34.9),
                                  ("Apdipositas Grad II", 35.0, 39.9), ("Adipositas Grad III", 40.0, 1000.0)),
                          "female": (("FEHLER", None), ("Untergewicht", 0.0, 19.0), ("Normalgewicht", 19.0, 23.9),
                                     ("Übergewicht", 24.0, 29.9),
                                     ("Starkes Übergewicht(Apdipositas Grad I)", 30.0, 34.9),
                                     ("Apdipositas Grad II", 35.0, 39.9), ("Adipositas Grad III", 40.0, 1000.0))}

        self.idealweight_table = ((19.0, 24.0, 19.0, 24.0), (25, 34, 20, 25), (35, 44, 21, 26), (45, 54, 23, 28),
                                  (65, 130, 24, 29))

    def set_ideal(self) -> None:
        for element in self.idealweight_table:
            if self.age >= element[0] and self.age <= element[1]:
                self.idealweight_low = self.size**2 * element[2]
                self.idealweight_high = self.size**2 * element[3]
                self.idealweight = round((self.idealweight_low + self.idealweight_high)/2, 1)

    def get_ideal(self) -> float:
        return self.idealweight

    def set_result(self) -> None:
        counter = 1
        result = 0
        bmitable = self.BMI_table["no_sex"]
        if self.sex == "male":
            bmitable = self.BMI_table["male"]
        if self.sex == "female":
            bmitable = self.BMI_table["female"]
        for element in bmitable[1:]:
            if self.bmi >= element[1] and self.bmi <= element[2]:
                self.result = bmitable[counter][0]
            counter = counter + 1
        return

    def get_result(self) -> float:
        return self.result

    def set_bmi(self):
        self.bmi = round(self.weight / (self.size**2), 1)



sex = str(input("Sex: "))
weight = float(input("Weight in kg: "))
size = ((float(input("Size in cm: "))) / 100)
age = float(input("Alter in Jahren: "))
BMI = BMIcalculation(sex, weight, size, age)
BMI.set_bmi()
BMI.set_result()
BMI.set_ideal()
