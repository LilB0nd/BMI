from noname import Panel
import wx


class BMIcalc(Panel):
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


    def set_age(self, age: int) -> None:
        """ Set new age
        :param age: new age
        """
        self.age = age
        return None

    def get_sex(self) -> str:
        """ get current sex as 'm' or 'f'
        :return: current sex
        """
        return sex

    def set_sex(self) -> None:
        """ Set new sex
        :param sex: new sex as 'm' or 'f'
        """
        if self.male_button.GetValue():
            sex = "MALE"
        elif self.female_button.GetValue():
            sex = "FEMALE"
        return None

    def get_size(self) -> float:
        """ get current size
        :return: current size in meters
        """
        return self.size

    def set_size(self) -> None:
        """ Set new size in meters
        :param size: new size
        """
        self.size = self.input_size.GetValue()

    def get_weight(self) -> float:
        """ get current weight
        :return: current weight in kg
        """
        pass # TODO

    def set_weight(self, weight: float) -> None:
        """ Set new weight in meters
        :param weight: new weight
        """
        self.weight = self.input_weight.GetValue()

    def get_ideal_weight(self) -> float:
        """ calculate ideal weight
        :return: ideal weight in gk
        """
        pass  # TODO

    def click_exit(self, event):
        self.Parent.Destroy()


app = wx.App()
frm = wx.Frame(None, title="BMI Rechner", size=wx.Size(350, 270))
pln = BMIcalc(frm)
frm.Show()
app.MainLoop()
