import wx
import wx.lib.intctrl
import json

class bucky(wx.Frame):
    
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="profiel calculator", pos=wx.DefaultPosition, size=(600, 400))
        self.panel = wx.Panel(self)

        #size button
        self.ButtonSize7 = wx.RadioButton(self.panel, label = "7mm")
        self.ButtonSize10 = wx.RadioButton(self.panel, label = "10mm")
        self.ButtonSize7.SetValue(True)

        self.input_names = ["height top", "height bottom", "width", "depth"]

        #next for what input
        self.HeightTop = wx.StaticText(self.panel, label="height top")
        self.HeightBottom = wx.StaticText(self.panel, label="height bottom")
        self.Width = wx.StaticText(self.panel, label="width")
        self.Depth = wx.StaticText(self.panel, label="depth")
        self.CalcText = wx.StaticText(self.panel, label="calculations:")

        self.inputs = [0] * 4
        self.calc = [0] * 4

        for i, input in enumerate(self.inputs):    
            self.inputs[i] = wx.lib.intctrl.IntCtrl(self.panel, value=0, allow_none=False, allow_long=False, size=(70, -1))
       
        #calculations display at:
        for i, calc in enumerate(self.calc):
            self.calc[i] = wx.StaticText(self.panel, label="")

        #calculate button
        self.button = wx.Button(self.panel, size=(70,-1), label="calculate")
        self.pre_button = wx.Button(self.panel, size=(70,-1), label="previous")

        #error Text
        self.error = wx.StaticText(self.panel, label="")
        # self.error.SetForegroundColour(wx.RED)

        #sizer setup
        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(self.panel, 1, wx.ALL | wx.EXPAND)  
        self.sizer = wx.GridBagSizer(5, 5)
        
        for i, input in enumerate(self.inputs):
            self.sizer.Add(input,(i+1,1))

        for i, input in enumerate(self.calc):
            self.sizer.Add(input,(i+1,2))

        self.sizer.Add(self.ButtonSize7, (0,0))
        self.sizer.Add(self.ButtonSize10, (0,1))
        self.sizer.Add(self.CalcText, (0,2))
        self.sizer.Add(self.HeightTop, (1,0))
        self.sizer.Add(self.HeightBottom, (2,0))
        self.sizer.Add(self.Depth, (3,0))
        self.sizer.Add(self.Width, (4,0))
        self.sizer.Add(self.error, (5,0))
        self.sizer.Add(self.button, (5,1))
        self.sizer.Add(self.pre_button,(5,2))

        #border for sizer
        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, 1, wx.ALL | wx.EXPAND, 5)

        #Use the sizers
        self.panel.SetSizerAndFit(self.border)  
        self.SetSizerAndFit(self.windowSizer)

        #button
        self.button.Bind(wx.EVT_BUTTON, self.OnButton)
        self.Bind(wx.EVT_BUTTON, self.on_show_data, self.pre_button)
    #define button
    def OnButton(self, e):
        self.clean()

        self.values = []
        buttonValue = self.ButtonSize7.GetValue()
        for input in self.inputs:
            self.values.append(input.GetValue())

        #calculations dictionary
        calculations = {
            "7mm": [-36,-36,-41,8],  #7mm
            "10mm": [-32,-32,-39,0]  #10mm
        }
        if buttonValue:
            profile_type = "7mm"
        elif not buttonValue:
            profile_type = "10mm"
        else:
            print("error")
            return
        
        self.answer = [0] * 4
        for i, value in enumerate(self.values):
            self.answer[i] = self.values[i] + calculations[profile_type][i]
            

        #error check
        for i, calc in enumerate(self.calc):
            if self.answer[i] < 1:
                self.error.SetLabel(f"error")
                self.calc[i].SetForegroundColour(wx.RED)
                self.calc[i].SetLabel(str(self.answer[i]))
        #if no error
            else:   
                self.calc[i].SetLabel(str(self.answer[i]))
                self.calc[i].SetForegroundColour(wx.WHITE)
        
        
        calculation_data = {
            "ProfileType": profile_type,
            "Values": self.values
        }

        db_function(calculation_data)

    

    def on_show_data(self, event):
        # Create a new window to display data
        data_window = DataWindow(parent = None, id = -1)
        data_window.Show()
    
        

    #text clearen
    def clean(self):
        self.error.SetLabel("")

        for i, calc in enumerate(self.calc):
            self.calc[i].SetLabel("")



#-------------------------------------------------------------------------------#
#oude calculaties window
class DataWindow(wx.Frame):
        
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="history", pos=wx.DefaultPosition, size=(600, 400))
        self.panel = wx.Panel(self)
        self.previous = 0
        
        self.prev_button = wx.Button(self.panel, size=(24,-1), label="<")
        self.next_button = wx.Button(self.panel, size=(24,-1), label=">")

        self.dspl = [0] * 4
        for i, dspl in enumerate(self.dspl):
            self.dspl[i] = wx.StaticText(self.panel, label="")

        self.history = wx.StaticText(self.panel, label="history:")
        self.HeightTop = wx.StaticText(self.panel, label="height top")
        self.HeightBottom = wx.StaticText(self.panel, label="height bottom")
        self.Width = wx.StaticText(self.panel, label="width")
        self.Depth = wx.StaticText(self.panel, label="depth")
        
        
        self.back = [0] * 4
        for i, back in enumerate(self.back):
            self.back[i] = wx.StaticText(self.panel, label="")
        
        #sizer setup
        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(self.panel, 1, wx.ALL | wx.EXPAND)  
        self.sizer = wx.GridBagSizer(5, 5)
        self.sizer.Add(self.HeightTop, (1,0))
        self.sizer.Add(self.HeightBottom, (2,0))
        self.sizer.Add(self.Depth, (3,0))
        self.sizer.Add(self.Width, (4,0))
        self.sizer.Add(self.history, (0,0))
        self.sizer.Add(self.prev_button,(5,3))
        self.sizer.Add(self.next_button,(5,4))
        for i, input in enumerate(self.back):
            self.sizer.Add(input,(i+1,2))
        

        self.Bind(wx.EVT_BUTTON, self.on_show_prev, self.prev_button)
        self.Bind(wx.EVT_BUTTON, self.on_show_next, self.next_button)

        #border for sizer
        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, 1, wx.ALL | wx.EXPAND, 5)

        #Use the sizers
        self.panel.SetSizerAndFit(self.border)  
        self.SetSizerAndFit(self.windowSizer)
    def on_show_prev(self, e):
        self.previous -= 1
        print("prev")
        for i, back in enumerate(self.back):
            self.back[i].SetLabel(str("prev"))

        
    def on_show_next(self, e):
        print("next")
        for i, back in enumerate(self.back):
            self.back[i].SetLabel(str("next"))
        
        
#-------------------------------------------------------------------------------#


#database
def db_function(new_calculation):
       fileDir = "fcc/data/BackLog.json"
       data = get_data(fileDir)
       data["calculations"].append(new_calculation)
       write_data(fileDir,data)

def get_data(fileDir):
    
    with open(fileDir, "r") as json_file:
        data = json.load(json_file)

    print(data)
    print(json.dumps(data))
    print(json.dumps(data, indent=1))

    return data
        
def write_data(fileDir, data):
    with open(fileDir, "w") as json_file:
        json.dump(data, json_file, indent=4)

#run program
if __name__ == "__main__":
    app = wx.App()
    frame = bucky(parent = None, id = -1)   
    frame.Show()
    app.MainLoop()
