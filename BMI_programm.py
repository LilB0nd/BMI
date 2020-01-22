from noname import Panel
import wx
#from types import Optional

#class BMIclac(Panel):
    #def set_table(self):
     #   self.BMItable = (("Untergewicht", ">18.4"), ("Normalgewicht", 18.5, 24.9), ("Übergewicht", 25, 29.9),
      #                   ("Starkes Übergewicht(Apdipositas Grad I)", 30, 34.9),("Apdipositas Grad II", 35, 39.9),
       #                  ("Adipositas Grad III", ">40"))
        #if self.BMItable[0]:
         #   print(self.BMItable)
#
    #def set_bmi(#self):
        #pass

class BMIprocessing(Panel):
    def get_inputs(self):
        size = self.input_size.GetValue()
        weight = self.input_weight.GetValue()
        age = self.input_age.GetValue()
        return [size,weight,age]

    def click_calc( self, event):
        self.output_bewertung.SetLabelMarkup("Zu Fett")
        self.output_BMI.SetLabelMarkup("over 9000")
        self.output_idealgewicht.SetLabelMarkup("75")

    def click_exit(self, event):
        self.Parent.Destroy()



app = wx.App()
frm = wx.Frame(None, title="BMI Rechner", size=wx.Size(350, 270),
               style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
pln = BMIprocessing(frm)
#BMIclac.set_bmi()
frm.Show()
app.MainLoop()
