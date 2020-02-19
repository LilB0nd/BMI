from noname import Panel
import wx
from typing import Optional


class BMIcalculation:
    def set_size(self, size: float) -> None:
        self.size = size/100
        return None

    def get_size(self) -> float:
        return self.size

    def set_age(self, age: Optional[int]) -> None:
        self.age = age
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

    def get_bmi(self) -> float:
        return self.bmi

    def set_category(self) -> None:
        BMItable = {None: (("FEHLER", None), ("Untergewicht", 0.0, 18.4), ("Normalgewicht", 18.5, 24.9),
                           ("Übergewicht", 25.0, 29.9), ("Starkes Übergewicht(Apdipositas Grad I)", 30.0, 34.9),
                           ("Apdipositas Grad II", 35.0, 39.9), ("Adipositas Grad III", 40.0, 200.0)),
                    "male": (("FEHLER", None), ("Untergewicht", 0.0, 20.0), ("Normalgewicht", 20.0, 24.9),
                             ("Übergewicht", 25.0, 29.9), ("Starkes Übergewicht(Apdipositas Grad I)", 30.0, 34.9),
                             ("Apdipositas Grad II", 35.0, 39.9), ("Adipositas Grad III", 40.0, 200.0)),
                    "female": (("FEHLER", None), ("Untergewicht", 0.0, 19.0), ("Normalgewicht", 19.0, 23.9),
                               ("Übergewicht", 24.0, 29.9),
                               ("Starkes Übergewicht(Apdipositas Grad I)", 30.0, 34.9),
                               ("Apdipositas Grad II", 35.0, 39.9), ("Adipositas Grad III", 40.0, 200.0))}
        counter = 1
        result = 0
        self.sex = "male"
        bmitable = BMItable[None]
        if self.sex == "male":
            bmitable = BMItable["male"]
        if self.sex == "female":
            bmitable = BMItable["female"]
        for element in bmitable[1:]:
            if self.bmi > element[1] and self.bmi < element[2]:
                result = counter
            counter = counter + 1
        self.category = bmitable[result][0]

    def get_category(self) -> str:
        return self.category

    def set_ideal(self) -> None:
        idealweight_table = ((19, 24, 19, 24), (25, 34, 20, 25), (35, 44, 21, 26), (45, 54, 23, 28),
                             (65, 130, 24, 29))
        for element in idealweight_table:
            if self.age >= element[0] and self.age <= element[1]:
                idealweight_low = self.size**2 * element[2]
                idealweight_high = self.size**2 * element[3]
                self.idealweight = round((idealweight_low + idealweight_high)/2, 1)
        return None

    def get_ideal(self) -> float:
        return self.idealweight


class BMIprocessing(Panel):
    def my_init_(self, BMIcalc):
        self.BMIcalc = BMIcalc

    def click_calc(self, event):
        self.BMIcalc.set_bmi()
        self.BMIcalc.set_category()
        self.BMIcalc.set_ideal()
        category = self.BMIcalc.get_category()
        bmi = str(self.BMIcalc.get_bmi())
        ideal = str(self.BMIcalc.get_ideal())
        self.output_raiting.SetLabelMarkup(category)
        self.output_BMI.SetLabelMarkup(bmi)
        self.output_idealweight.SetLabelMarkup(ideal)

    def click_exit(self, event):
        self.Destroy()
        exit()

    def on_size_input(self, event):
        try:
            self.input_size.SetForegroundColour(wx.BLACK)
            input_size = float(self.input_size.GetValue())
            self.BMIcalc.set_size(size=input_size)
        except ValueError:
            self.input_size.SetForegroundColour(wx.RED)
        self.input_size.Refresh()

    def on_weight_input(self, event):
        try:
            self.input_weight.SetForegroundColour(wx.BLACK)
            input_weight = int(self.input_weight.GetValue())
            self.BMIcalc.set_weight(weight=input_weight)
        except ValueError:
            self.input_weight.SetForegroundColour(wx.RED)
        self.input_weight.Refresh()

    def on_age_input(self, event):
        try:
            self.input_age.SetForegroundColour(wx.BLACK)
            input_age = int(self.input_age.GetValue())
            self.BMIcalc.set_age(age=input_age)

        except ValueError:
            self.input_age.SetForegroundColour(wx.RED)
        self.input_age.Refresh()


app = wx.App()
frm = wx.Frame(None, title="BMI Rechner", size=wx.Size(360, 270),
               style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
BMIcalc = BMIcalculation()
pln = BMIprocessing(frm)
pln.my_init_(BMIcalc)
frm.Show()
app.MainLoop()