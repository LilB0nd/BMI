from noname import Panel
import wx
from typing import Optional


class BMIcalculation:
    def __init__(self):
        self.bmi_table = {None: (("FEHLER", None), ("Untergewicht", 0.0, 18.4), ("Normalgewicht", 18.5, 25.0),
                                 ("Übergewicht", 25.0, 30.0), ("Starkes Übergewicht(Adipositas Grad I)", 30.0, 35.0),
                                 ("Adipositas Grad II", 35.0, 40), ("Adipositas Grad III", 40.0, 200.0)),
                          "male": (("FEHLER", None), ("Untergewicht", 0.0, 20.0), ("Normalgewicht", 20.0, 25.0),
                                   ("Übergewicht", 25.0, 30.0), ("Starkes Übergewicht(Adipositas Grad I)", 30.0, 35.0),
                                   ("Adipositas Grad II", 35.0, 39.9), ("Adipositas Grad III", 40.0, 200.0)),
                          "female": (("FEHLER", None), ("Untergewicht", 0.0, 19.0), ("Normalgewicht", 19.0, 24.0),
                                     ("Übergewicht", 24.0, 30.0),
                                     ("Starkes Übergewicht(Adipositas Grad I)", 30.0, 35.0),
                                     ("Adipositas Grad II", 35.0, 40.0), ("Adipositas Grad III", 40.0, 200.0))}
        self.size = 1
        self.bmi = 0
        self.age = None
        self.weight = 0
        self.ideal_weight = 0
        self.category = None
        self.sex = None

    def set_size(self, size: float) -> None:
        self.size = size / 100
        return None

    def set_age(self, age: Optional[int]) -> None:
        self.age = age
        return None

    def get_age(self):
        return self.age

    def set_weight(self, weight: float) -> None:
        self.weight = weight
        return None

    def get_weight(self) -> float:
        return self.weight

    def set_sex(self, sex: Optional[str]) -> None:
        self.sex = sex
        return None

    def get_sex(self):
        return self.sex

    def set_bmi(self) -> None:
        self.bmi = round(self.weight / (self.size ** 2), 1)
        return None

    def get_bmi(self) -> float:
        return self.bmi

    def set_category(self) -> None:
        try:
            counter = 1
            result = 0
            bmitable = self.bmi_table[None]
            if self.sex == "male":
                bmitable = self.bmi_table["male"]
            if self.sex == "female":
                bmitable = self.bmi_table["female"]
            for element in bmitable[1:]:
                if self.bmi > element[1] < element[2]:
                    result = counter
                counter = counter + 1
            self.category = bmitable[result][0]
        except ZeroDivisionError:
            self.category = "Fehler"

    def get_category(self) -> str:
        return self.category

    def set_ideal(self) -> None:
        age_table = ((25, 34, 1), (35, 44, 2), (45, 54, 3), (55, 65, 4), (65, 130, 5))
        ideal_bmi = 0
        if self.sex == "male":
            ideal_bmi = 22.5
        elif self.sex == "female":
            ideal_bmi = 21.5
        elif self.sex == "no_sex":
            ideal_bmi = 21.7
        print(ideal_bmi)
        if self.age:
            for element in age_table:
                if self.age >= element[0] and self.bmi <= element[1]:
                    ideal_bmi = ideal_bmi + element[2]
            self.ideal_weight = round(self.size ** 2 * ideal_bmi, 2)
        else:
            self.ideal_weight = round(float(self.size ** 2 * ideal_bmi), 2)
        return None

    def get_ideal(self) -> float:
        return self.ideal_weight


class BMIprocessing(Panel):
    def __init__(self, bmicalc, parent):
        super().__init__(parent)
        self.BMIcalc = bmicalc
        self.age_input = None

    def sex_button(self):
        if self.male_button.GetValue():
            sex = "male"

        elif self.female_button.GetValue():
            sex = "female"

        else:
            sex = None

        self.BMIcalc.set_sex(sex)

    def click_calc(self, event):
        self.sex_button()
        self.BMIcalc.set_bmi()
        self.BMIcalc.set_category()
        self.BMIcalc.set_ideal()

        category = self.BMIcalc.get_category()
        bmi = str(self.BMIcalc.get_bmi())
        ideal = str(self.BMIcalc.get_ideal())
        if "untergewicht" in category.lower() or "übergewicht" in category.lower():
            self.output_raiting.SetForegroundColour((255, 128, 0))
        elif "normalgewicht" in category.lower():
            self.output_raiting.SetForegroundColour(wx.GREEN)
        else:
            self.output_raiting.SetForegroundColour(wx.RED)

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
            self.output_raiting.SetLabelMarkup(" ")

        except ValueError:
            self.output_raiting.SetForegroundColour(wx.RED)
            self.output_raiting.SetLabelMarkup("FEHLER")
            self.output_BMI.SetLabelMarkup(" ")
            self.output_idealweight.SetLabelMarkup(" ")
            self.input_size.SetForegroundColour(wx.RED)
        self.input_size.Refresh()

    def on_weight_input(self, event):
        try:
            self.input_weight.SetForegroundColour(wx.BLACK)
            input_weight = float(self.input_weight.GetValue())
            self.BMIcalc.set_weight(weight=input_weight)
            self.output_raiting.SetLabelMarkup(" ")

        except ValueError:
            self.output_raiting.SetForegroundColour(wx.RED)
            self.output_raiting.SetLabelMarkup("FEHLER")
            self.output_BMI.SetLabelMarkup(" ")
            self.output_idealweight.SetLabelMarkup(" ")
            self.input_weight.SetForegroundColour(wx.RED)
        self.input_weight.Refresh()

    def on_age_input(self, event):
        try:
            self.input_age.SetForegroundColour(wx.BLACK)
            input_age = int(self.input_age.GetValue())
            self.BMIcalc.set_age(age=input_age)
            self.output_raiting.SetLabelMarkup(" ")

        except ValueError:
            self.output_raiting.SetForegroundColour(wx.RED)
            self.output_raiting.SetLabelMarkup("FEHLER")
            self.output_BMI.SetLabelMarkup(" ")
            self.output_idealweight.SetLabelMarkup(" ")
            self.input_age.SetForegroundColour(wx.RED)
        self.input_age.Refresh()


app = wx.App()
frm = wx.Frame(None, title="BMI Rechner", size=wx.Size(360, 270),
               style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
BMIcalc = BMIcalculation()
pln = BMIprocessing(BMIcalc, frm)
frm.Show()
app.MainLoop()
