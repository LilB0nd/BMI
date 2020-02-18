from noname import Panel
import wx
from typing import Optional


class BMIcalculation:

    def __init__(self):
        self.idealweight = None
        self.idealweight_low = None
        self.idealweight_high = None
        self.bmi = None
        self.result = None
        self.BMItable = {None: (("FEHLER", None), ("Untergewicht", 0.0, 18.4), ("Normalgewicht", 18.5, 24.9),
                                ("Übergewicht", 25.0, 29.9), ("Starkes Übergewicht(Apdipositas Grad I)", 30.0, 34.9),
                                ("Apdipositas Grad II", 35.0, 39.9),("Adipositas Grad III", 40.0, 200.0)),
                         "male": (("FEHLER", None), ("Untergewicht", 0.0, 20.0), ("Normalgewicht", 20.0, 24.9),
                                  ("Übergewicht", 25.0, 29.9), ("Starkes Übergewicht(Apdipositas Grad I)", 30.0, 34.9),
                                  ("Apdipositas Grad II", 35.0, 39.9), ("Adipositas Grad III", 40.0, 200.0)),
                         "female": (("FEHLER", None), ("Untergewicht", 0.0, 19.0), ("Normalgewicht", 19.0, 23.9),
                                    ("Übergewicht", 24.0, 29.9),
                                    ("Starkes Übergewicht(Apdipositas Grad I)", 30.0, 34.9),
                                    ("Apdipositas Grad II", 35.0, 39.9), ("Adipositas Grad III", 40.0, 200.0))}
        self.idealweight_table = ((19, 24, 19, 24), (25, 34, 20, 25), (35, 44, 21, 26), (45, 54, 23, 28),
                                  (65, 130, 24, 29))

    def set_size(self, size: float) -> None:
        self.size = size
        print(size)
        return None

    def get_size(self) -> float:
        return self.size

    def set_age(self, age: Optional[int]) -> None:
        self.age = age
        print(age)
        return None

    def get_age(self) -> int:
        return self.age

    def set_weight(self, weight: float) -> None:
        self.weight = weight
        return None

    def get_weight(self) -> float:
        return self.weight

    def set_sex(self, sex: Optional[str]) -> None:
        self.sex = sex
        return None

    def get_sex(self) -> str:
        return self.sex

    def set_bmi(self) -> None:
        self.bmi = round(self.weight/(self.size**2), 1)
        return None

    def get_bmi(self) -> float:
        return self.bmi

    def set_category(self) -> None:
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
        return None

    def get_category(self) -> str:
        return self.result

    def set_ideal(self) -> None:
        for element in self.idealweight_table:
            if self.age >= element[0] and self.age <= element[1]:
                self.idealweight_low = self.size**2 * element[2]
                self.idealweight_high = self.size**2 * element[3]
                self.idealweight = round((self.idealweight_low + self.idealweight_high)/2, 1)
        return None

    def get_ideal(self) -> float:
        return self.idealweight


class BMIprocessing(Panel):

    def get_inputs(self):
        return [self.weight, self.size, self.age]

    def set_output(self):
        self.category = self.BMIcalc.get_category()
        self.BMI = self.BMIcalc.get_bmi()
        self.idealweight = self.BMIcalc.get_ideal()

    def click_calc(self, event):
        self.BMIcalc = BMIcalculation()
        self.BMIcalc.get_bmi()
        print(self.category)
        self.output_raiting.SetLabelMarkup(self.category)
        self.output_BMI.SetLabelMarkup(self.BMI)
        self.output_idealweight.SetLabelMarkup( self.idealweight)

    def click_exit(self, event):
        self.Destroy()
        exit()

    def on_size_input(self, event):
    # Zurück zu schwarz macen
        self.input_size.SetForegroundColour(wx.BLACK)
        try:
            input_size = float(self.input_size.GetValue())
            BMIcalc.set_size(size = input_size)
        except ValueError:
            self.input_size.SetForegroundColour(wx.RED)
              # set text color
        event.Skip()

    def on_weight_input(self, event):
        # Zurück zu schwarz machen
        try:
            self.input_weight.SetForegroundColour(wx.BLACK)
            self.weight = int(self.input_weight.GetValue())
        except ValueError:
            self.input_weight.SetForegroundColour(wx.RED)

    def on_age_input(self, event):
        # Zurück zu schwarz machen
        try:
            self.input_age.SetForegroundColour(wx.BLACK)
            self.age = int(self.input_age.GetValue())

        except ValueError:
            self.input_age.SetForegroundColour(wx.RED)


app = wx.App()
frm = wx.Frame(None, title="BMI Rechner", size=wx.Size(360, 270),
               style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
pln = BMIprocessing(frm)
BMIcalc = BMIcalculation()
frm.Show()
app.MainLoop()




