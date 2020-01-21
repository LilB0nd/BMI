from noname import Panel
import wx
from typing import Optional

class BmiCalc:
    """Interface for BMI Calculation"""

    def get_bmi(self) -> float:
        """ :return: current BMI """
        pass  # TODO

    def get_category(self) -> str:
        """
        :return: current weight category as string
        """
        pass  # TODO

    def get_age(self) -> int:
        """ get current age
        :return: current age
        """
        pass  # TODO

    def set_age(self, age: Optional[int]) -> None:
        """ Set new or reset age
        :param age: new age or None to reset
        """
        pass  # TODO

    def get_sex(self) -> str:
        """ get current sex as 'm' or 'f'
        :return: current sex
        """
        pass  # TODO

    def set_sex(self, sex: Optional[str]) -> None:
        """ Set new or reset sex
        :param sex: new sex as 'm' or 'f' or None to reset
        """
        pass  # TODO

    def get_size(self) -> float:
        """ get current size
        :return: current size in meters
        """
        pass  # TODO

    def set_size(self, size: float) -> None:
        """ Set new size in meters
        :param size: new size
        """
        pass  # TODO

    def get_weight(self) -> float:
        """ get current weight
        :return: current weight in kg
        """
        pass  # TODO

    def set_weight(self, weight: float) -> None:
        """ Set new weight in meters
        :param weight: new weight
        """
        pass  # TODO

    def get_ideal_weight(self) -> float:
        """ calculate ideal weight
        :return: ideal weight in gk
        """
        pass  # TODO


class BMIprocessing(Panel):
    def get_inputs(self):
        size = self.input_size.GetValue()
        weight = self.input_weight.GetValue()
        age = self.input_age.GetValue()

    def click_calc( self, event,BMI,Ideal_weight,result ):#Fehler
        self.output_bewertung.SetLabelMarkup(result)
        self.output_BMI.SetLabelMarkup(BMI)
        self.output_idealgewicht.SetLabelMarkup(Ideal_weight)

    def click_exit(self, event):
        self.Parent.Destroy()
        print(self.input_size.GetValue())


app = wx.App()
frm = wx.Frame(None, title="BMI Rechner", size=wx.Size(350, 270))
pln = BMIprocessing(frm)
frm.Show()
app.MainLoop()
