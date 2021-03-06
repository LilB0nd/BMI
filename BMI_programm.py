from BMI_GUI import Panel
import wx
from typing import Optional


class BMIcalculation:
    def __init__(self):
        self.size = 0
        self.weight = 0.0
        self.age = None
        self.sex = None

        self.bmi = 0.0
        self.ideal_weight = 0.0
        self.category = None

    def set_size(self, size: float) -> None:
        """
        Hier wird die Größe difieniert und durch 100 geteilt, um die Größe in der Einheit m zu haben anstatt in cm.
        :param size: Die Größe die von der GUI hier übergeben wird.
        """
        try:
            self.size = size / 100  # Hier wird die Größe von cm in Meter umgewandelt
        except ZeroDivisionError:  # Dient zur Fehlervermeidung
            pass
        return None

    def set_age(self, age: Optional[int]) -> None:
        """
        age wird mithilfe von self in der komplette Klasse nutzbar gemacht
        :param age:
        """
        self.age = age
        return None

    def get_age(self) -> Optional[int]:
        """
        Das Alter wird returned
        :return: age(int oder float)
        """
        return self.age

    def set_weight(self, weight: float) -> None:
        """
        weight wird mithilfe von self in der komplette Klasse nutzbar gemacht
        :param weight:
        """
        self.weight = weight
        return None

    def get_weight(self) -> float:
        """
        Das Gewicht wird returned
        :return: weight(float)
        """
        return self.weight

    def set_sex(self, sex: Optional[str]) -> None:
        """
        Sex wird mithilfe von self in der komplette Klasse nutzbar gemacht.
        Sex ist ein string oder None
        :param sex:
        """
        self.sex = sex
        return None

    def get_sex(self) -> Optional[str]:
        """
        Das Geschlecht wird returned, entweder in Form eines str oder ein None
        :return: sex(str oder None)
        """
        return self.sex

    def set_bmi(self) -> None:
        """
        Hier wird der BMI errechnet, da es zum ZeroDivisionError kommen kann gibt es try und except ZeroDiviionErrror
        :return:
        """
        try:
            self.bmi = round(self.weight / (self.size ** 2), 1)  # Hier wird der BMI errechnet
        except ZeroDivisionError:  # Dient zur Fehlervermeidung
            pass
        return None

    def get_bmi(self) -> float:
        """
        Der Body-MasssIndex wird returned
        :return: bmi(float)
        """
        return self.bmi

    def set_category(self) -> None:
        """
        Hier wird sich Gewichtsklasse herrausgesucht anhand des Geschlechts und des BMIs
        Die Werte aus den Tupel kommen von der Internetseite:
        http://www.spiegel.de/gesundheit/ernaehrung/bmi-rechner-so-ermitteln-sie-ihren-body-mass-index-a-824673.html
        """
        counter = 0
        result = 0
        if self.sex == "male":
            bmi_tuple = (("FEHLER", None), ("Untergewicht", 0.1, 20.0), ("Normalgewicht", 20.0, 25.0),
                         ("Übergewicht", 25.0, 30.0), ("Starkes Übergewicht(Adipositas Grad I)", 30.0, 35.0),
                         ("Adipositas Grad II", 35.0, 39.9), ("Adipositas Grad III", 40.0, 200.0))
        elif self.sex == "female":
            bmi_tuple = (("FEHLER", None), ("Untergewicht", 0.1, 19.0), ("Normalgewicht", 19.0, 24.0),
                         ("Übergewicht", 24.0, 30.0), ("Starkes Übergewicht(Adipositas Grad I)", 30.0, 35.0),
                         ("Adipositas Grad II", 35.0, 40.0), ("Adipositas Grad III", 40.0, 200.0))
        else:
            bmi_tuple = (("FEHLER", None), ("Untergewicht", 0.1, 18.4), ("Normalgewicht", 18.5, 25.0),
                         ("Übergewicht", 25.0, 30.0), ("Starkes Übergewicht(Adipositas Grad I)", 30.0, 35.0),
                         ("Adipositas Grad II", 35.0, 40), ("Adipositas Grad III", 40.0, 200.0))

        for element in bmi_tuple[1:]:
            counter = counter + 1
            if element[1] <= self.bmi <= element[2]:  # Es wird geschaut ob der BMI zwischen diesen Wertebereich ist
                result = counter

        self.category = bmi_tuple[result][0]

    def get_category(self) -> str:
        """
        Die Bewertung des BMI wird returned
        :return: category(str)
        """
        return self.category

    def set_ideal(self) -> None:
        """
        Hier wird das idealgewicht berechnet.
        """
        age_table = ((25, 34, 1), (35, 44, 2), (45, 54, 3), (55, 65, 4), (65, 130, 5))
        if self.sex == "male":
            ideal_bmi = 22.5
        elif self.sex == "female":
            ideal_bmi = 21.5
        else:
            ideal_bmi = 21.7
        if self.size != 0.0 and self.weight != 0.0:  # Dies dient dazu Fehler zu verhindern
            if self.age:
                for element in age_table:
                    if element[0] <= self.age <= element[1]:  # Es wird geschaut,
                        # ob das Alter zwischen diesen  Wertebereich ist
                        ideal_bmi = ideal_bmi + element[2]
                self.ideal_weight = round(self.size ** 2 * ideal_bmi, 2)
            else:
                self.ideal_weight = round(float(self.size ** 2 * ideal_bmi), 2)
        else:
            self.ideal_weight = 0.0
            return None

    def get_ideal(self) -> float:
        """
        Das Idealgewicht für die angegebene Größe, Gewicht und Alter wird zurückgeben
        :return: ideal_weight(float)
        """
        return self.ideal_weight


class BMIprocessing(Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.BMIcalc = BMIcalculation()

    def sex_buttons(self):
        """
        Holt sich das ausgewählte Geschlecht aus der Gui und gibt sie an die Instanz der Klasse BMIcalculation weiter
        :return: Das Geschlecht das ausgewählt wurde wird der Klasse BMIcalculation übergeben
        """
        if self.male_button.GetValue():
            sex = "male"

        elif self.female_button.GetValue():
            sex = "female"

        else:
            sex = None

        self.BMIcalc.set_sex(sex)

    def click_calc(self, event):
        """
        Dient primär dazu die Outputs zu tätigen
        """
        self.sex_buttons()  # Geschlecht bestimmen

        self.BMIcalc.set_bmi()  # Werte werden ermittelt
        self.BMIcalc.set_category()
        self.BMIcalc.set_ideal()

        category = self.output_rating.GetLabel()  # Die vorherigen Werte werden Zwischen gespeichert
        ideal = self.output_idealweight.GetLabel()
        bmi = self.output_BMI.GetLabel()

        if category != "FEHLER":
            category = self.BMIcalc.get_category()
            bmi = str(self.BMIcalc.get_bmi())
            ideal = str(self.BMIcalc.get_ideal())

        if "untergewicht" in category.lower() or "übergewicht" in category.lower():  # Schriftfarbe wird gesetzt
            self.output_rating.SetForegroundColour((255, 128, 0))
        elif "normalgewicht" in category.lower():
            self.output_rating.SetForegroundColour(wx.GREEN)
        else:
            self.output_rating.SetForegroundColour(wx.RED)

        self.output_idealweight.SetLabelMarkup(ideal)  # Ausgaben werden getätigt
        self.output_rating.SetLabelMarkup(category)
        self.output_BMI.SetLabelMarkup(bmi)

    def click_exit(self, event):
        """
        Schließt das Fenster und beendet das Programm
        """
        exit()

    def on_size_input(self, event):
        """
        Guckt ob der Eingabewert eine Zahl ist und gibt sie an die Instanz der Klasse BMIcalculation weiter,
        wenn der Eingabewert keine Zahl ist wird er rot und es werden die error_outputs ausgegeben
        """
        try:
            self.input_size.SetForegroundColour(wx.BLACK)
            input_size = float(self.input_size.GetValue())
            self.BMIcalc.set_size(size=input_size)
            self.clear_outputs()

        except ValueError:
            self.error_outputs()
        self.input_size.Refresh()

    def on_weight_input(self, event):
        """
        Guckt ob der Eingabewert eine Zahl und gibt sie an die Instanz der Klasse BMIcalculation weiter,
        wenn der Eingabewert keine Zahl ist wird er rot und es werden die error_outputs ausgegeben
        """
        try:
            self.input_weight.SetForegroundColour(wx.BLACK)
            input_weight = float(self.input_weight.GetValue())
            self.BMIcalc.set_weight(weight=input_weight)
            self.clear_outputs()

        except ValueError:
            self.error_outputs()
        self.input_weight.Refresh()

    def on_age_input(self, event):
        """
        Guckt ob der Eingabewert eine Zahl und gibt sie an die Instanz der Klasse BMIcalculation weiter,
        wenn der Eingabewert keine Zahl ist wird er rot und es werden die error_outputs ausgegeben
        Wenn kein Wert eingegeben wurde, wird der Wert 0 weitergegeben.
        """
        try:
            self.input_age.SetForegroundColour(wx.BLACK)
            if self.input_age.GetValue() == "":
                input_age = 0
            else:
                input_age = int(self.input_age.GetValue())
            self.BMIcalc.set_age(age=input_age)
            self.clear_outputs()

        except ValueError:
            self.error_outputs()
        self.input_age.Refresh()

    def clear_outputs(self):
        """
        Leert die ausgabe Beschriftungen
        """
        self.output_rating.SetLabelMarkup("")
        self.output_BMI.SetLabelMarkup("")
        self.output_idealweight.SetLabelMarkup("")

    def error_outputs(self):
        """
        Gibt “FEHLER” bei der Bewertung aus und
        setzt die ausgabe Beschriftungen von dem BMI und dem Idealgewicht auf 0
        """
        self.output_rating.SetForegroundColour(wx.RED)
        self.output_rating.SetLabelMarkup("FEHLER")
        self.output_BMI.SetLabelMarkup("0")
        self.output_idealweight.SetLabelMarkup("0")
        self.input_weight.SetForegroundColour(wx.RED)


app = wx.App()
frm = wx.Frame(None, title="BMI Rechner", size=wx.Size(370, 270),
               style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
pln = BMIprocessing(frm)
frm.Show()
app.MainLoop()
