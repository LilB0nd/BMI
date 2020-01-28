from noname import Panel
import wx


class BMIcalculation:
    def __init__(self, user_input):
        self.sex = "male"
        self.weight = user_input[1]
        self.size = user_input[0]
        # self.age = user_input[2]
        self.idealweight = None
        self.idealweight_low = None
        self.idealweight_high = None
        self.bmi = None
        self.result = None
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
        self.idealweight_table = ((19, 24, 19, 24), (25, 34, 20, 25), (35, 44, 21, 26), (45, 54, 23, 28), (65, 130, 24, 29))

    def set_ideal(self):
        for element in self.idealweight_table:
            if self.age >= element[0] and self.age <= element[1]:
                self.idealweight_low = self.size**2 * element[2]
                self.idealweight_high = self.size**2 * element[3]
                self.idealweight = round((self.idealweight_low + self.idealweight_high)/2, 1)

    def get_ideal(self):
        return self.idealweight

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
        self.result = bmitable[result][0]

    def get_result(self):
        return self.result

    def set_bmi(self):
        self.bmi = round(self.weight/(self.size**2), 1)

    def get_bmi(self):
        return self.bmi


class BMIprocessing(Panel):
    def get_inputs(self):
        print(self.input_size)
        if self.input_size.GetValue().isnumeric():
            size = self.input_size.GetValue()
            self.input_size.SetForegroundColour(wx.Colour(0, 0, 0))
        else:
            self.input_size.SetForegroundColour(wx.Colour(255, 0, 0))

        weight = self.input_weight.GetValue()
        age = self.input_age.GetValue()
        return [weight, age]  # [weight,size, age] in der Reihenfolge bitte

    def click_calc(self, event):
        self.output_raiting.SetLabelMarkup("Zu Fett")
        self.output_BMI.SetLabelMarkup("over 9000")
        self.output_idealweight.SetLabelMarkup("75")

    def click_exit(self, event):
        self.Parent.Destroy()


app = wx.App()
frm = wx.Frame(None, title="BMI Rechner", size=wx.Size(350, 270),
               style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
pln = BMIprocessing(frm)
input = BMIprocessing.get_inputs(pln)
BMIcalc = BMIcalculation(input)

frm.Show()
app.MainLoop()
