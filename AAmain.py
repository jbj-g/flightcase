import wx
import wx.lib.intctrl

class bucky(wx.Frame):
    
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="Number Input", pos=wx.DefaultPosition, size=(600, 400))
        self.panel = wx.Panel(self)

        #size button
        self.ButtonSize7 = wx.RadioButton(self.panel, label = "7mm")
        self.ButtonSize10 = wx.RadioButton(self.panel, label = "10mm")
        self.ButtonSize7.SetValue(True)
A
        #next for what input
        self.HeightTop = wx.StaticText(self.panel, label="height top")
        self.HeightBottom = wx.StaticText(self.panel, label="height bottom")
        self.Width = wx.StaticText(self.panel, label="width")
        self.Depth = wx.StaticText(self.panel, label="depth")
        self.CalcText = wx.StaticText(self.panel, label="calculations:")

        #inputs for ath
        self.Input1 = wx.lib.intctrl.IntCtrl(self.panel, value=0, allow_none=False, allow_long=False, size=(70, -1))
        self.Input2 = wx.lib.intctrl.IntCtrl(self.panel, value=0, allow_none=False, allow_long=False, size=(70, -1))
        self.Input3 = wx.lib.intctrl.IntCtrl(self.panel, value=0, allow_none=False, allow_long=False, size=(70, -1))
        self.Input4 = wx.lib.intctrl.IntCtrl(self.panel, value=0, allow_none=False, allow_long=False, size=(70, -1))

        #calculations display at:
        self.calc1 = wx.StaticText(self.panel, label="")
        self.calc2 = wx.StaticText(self.panel, label="")
        self.calc3 = wx.StaticText(self.panel, label="")
        self.calc4 = wx.StaticText(self.panel, label="")
    

        #calculate button
        self.button = wx.Button(self.panel, size=(70,-1), label="calculate")

        #error Text
        self.error = wx.StaticText(self.panel, label="")
        self.error.SetForegroundColour(wx.RED)


        #sizer setup
        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(self.panel, 1, wx.ALL | wx.EXPAND)  

        self.sizer = wx.GridBagSizer(5, 5)
        self.sizer.Add(self.ButtonSize7, (0,0))
        self.sizer.Add(self.ButtonSize10, (0,1))
        self.sizer.Add(self.CalcText, (0,3))
        self.sizer.Add(self.HeightTop, (1,0))
        self.sizer.Add(self.HeightBottom, (2,0))
        self.sizer.Add(self.Depth, (3,0))
        self.sizer.Add(self.Width, (4,0))
        self.sizer.Add(self.Input1, (1,1))
        self.sizer.Add(self.Input2, (2,1))
        self.sizer.Add(self.Input3, (3,1))
        self.sizer.Add(self.Input4, (4,1))
        self.sizer.Add(self.calc1, (1,3))
        self.sizer.Add(self.calc2, (2,3))
        self.sizer.Add(self.calc3, (3,3))
        self.sizer.Add(self.calc4, (4,3))
        self.sizer.Add(self.button, (5,1))
        self.sizer.Add(self.error, (5,2))

        #border for sizer
        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, 1, wx.ALL | wx.EXPAND, 5)

        #Use the sizers
        self.panel.SetSizerAndFit(self.border)  
        self.SetSizerAndFit(self.windowSizer)

        #get size
        

        self.button.Bind(wx.EVT_BUTTON, self.OnButton)

    def OnButton(self, e):
        buttonValue = self.ButtonSize7.GetValue()
        input1 = self.Input1.GetValue()
        input2 = self.Input2.GetValue()
        input3 = self.Input3.GetValue()
        input4 = self.Input4.GetValue()
        """"
        try:
            input1 = int(input1)
            input2 = int(input2)
            input3 = int(input3)
            input4 = int(input4)
            self.error.SetLabel("")

        except ValueError:
           self.error.SetLabel("Error")
        """
            


        if buttonValue:

            input1 -= 36
            input2 -= 36
            input3 -= 41
            input4 += 8

            self.calc1.SetLabel(str(input1))
            self.calc2.SetLabel(str(input2))
            self.calc3.SetLabel(str(input3))
            self.calc4.SetLabel(str(input4))
        
        else:
            
            input1 -= 32
            input2 -= 32
            input3 -= 39
            input4 += 0

            self.calc1.SetLabel(str(input1))
            self.calc2.SetLabel(str(input2))
            self.calc3.SetLabel(str(input3))
            self.calc4.SetLabel(str(input4))
        



if __name__ == "__main__":
    app = wx.App()
    frame = bucky(parent = None, id = -1)   
    frame.Show()
    app.MainLoop()
