import wx
import wx.lib.intctrl
import json
import math


print("gabriel sucks pp")
class bucky(wx.Frame):
    def __init__(self, parent, style):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="calculator", pos=wx.DefaultPosition, style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.panel = wx.Panel(self)
        self.InitUI() 
        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.data_window = None
        self.render = None

        #size button
        self.ButtonSize7 = wx.RadioButton(self.panel, label = "7mm")
        self.ButtonSize10 = wx.RadioButton(self.panel, label = "10mm")
        self.ButtonSize7.SetValue(True)

        self.input_names = ["height top", "height bottom", "width", "depth"]

        #next for what input
        self.HeightTop = wx.StaticText(self.panel, label="height top:")
        self.HeightBottom = wx.StaticText(self.panel, label="height bottom:")
        self.Width = wx.StaticText(self.panel, label="width:")
        self.Depth = wx.StaticText(self.panel, label="depth:")
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
        self.pre_button = wx.Button(self.panel, size=(70,-1), label="History")

        #error Text
        self.error = wx.StaticText(self.panel, label="")

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
            
        calculation_data = {
            "ProfileType": profile_type,
            "Values": self.values
        }
        db_function(calculation_data)

        errorCheck = False
        #error check
        for i, calc in enumerate(self.calc):
            
            if self.answer[i] < 1:
                errorCheck = True
                self.error.SetLabel(f"error")
                self.calc[i].SetForegroundColour(wx.RED)
                self.error.SetForegroundColour(wx.RED)
                self.calc[i].SetLabel(str(self.answer[i]))
                

        #if no error
            else:   
                self.calc[i].SetLabel(str(self.answer[i]))
                self.calc[i].SetForegroundColour(wx.WHITE)
        if not errorCheck:
            if self.render: 
                self.render.Close()
            self.render = DrawingFrame(parent = None, id = -1)
            x, y = self.GetPosition()
            self.render.SetPosition((x, y + 197))
            self.render.Show()
            self.render.SetSize((512, 394))
            self.render.SetMaxSize((512, 394))
            self.render.SetMinSize((512, 394))
            self.p_top    =  self.answer[0] #top
            self.p_bottom =  self.answer[1]  #bottom
            self.p_side   =  self.answer[2]  #side
            self.p_front  =  self.answer[3]  #front
    
                
               
    def on_show_data(self, event):
        # Create a new window to display data
        if self.data_window: 
                self.data_window.Close()
        self.data_window = DataWindow(parent = None, id = -1)
        first_window_size = self.GetSize()
        x, y = self.GetPosition()
        self.data_window.SetPosition((x + first_window_size[0], y))
        self.data_window.Show()
        self.data_window.SetSize((256, 197))

        
    def on_close(self, event):
        # Close the second window if it's open
        if self.data_window:
            self.data_window.Close()
        if self.render:
            self.render.Close()
        event.Skip()  


    def reset_data(self):
        default_data = {
            "calculations": [
                {
                    "ProfileType": "7mm",
                    "Values": [10, 10, 10, 10]
                }
            ]
        }

        with open("fcc/data/BackLog.json", 'w') as file:
            json.dump(default_data, file)
        if self.data_window: 
                self.data_window.Close()
                self.data_window = DataWindow(parent = None, id = -1)
                first_window_size = self.GetSize()
                x, y = self.GetPosition()
                self.data_window.SetPosition((x + first_window_size[0], y))
                self.data_window.Show()
                self.data_window.SetSize((256, 197))
    
                




    def InitUI(self):    
	 # Create a menu bar
        menubar = wx.MenuBar()
        history_menu = wx.Menu()
        reset_item = history_menu.Append(wx.ID_ANY, "Reset")
        self.Bind(wx.EVT_MENU, self.on_reset, reset_item)
        menubar.Append(history_menu, "History")
        self.SetMenuBar(menubar)

    def on_reset(self, event):
        self.reset_data()
               

    #text clearen
    def clean(self):
        self.error.SetLabel("")

        for i, calc in enumerate(self.calc):
            self.calc[i].SetLabel("")
    
    

#-------------------------------------------------------------------------------#
#history window
class DataWindow(wx.Frame):
    
        
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="history", pos=wx.DefaultPosition, style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.panel = wx.Panel(self)
        fileDir = "fcc/data/BackLog.json"
        data = get_data(fileDir)
        self.previous = len(data['calculations'])
        self.SetSize(wx.Size(256, 197))
        
 
        self.prev_button = wx.Button(self.panel, size=(24,-1), label="<")
        self.next_button = wx.Button(self.panel, size=(24,-1), label=">")
        self.ButtonSize7 = wx.RadioButton(self.panel, label = "7mm")
        self.ButtonSize10 = wx.RadioButton(self.panel, label = "10mm")
        self.ButtonSize7.SetValue(True)

        self.math = {
            "7mm": [-36,-36,-41,8],  #7mm
            "10mm": [-32,-32,-39,0]  #10mm
            }

        self.dspl = [0] * 4
        for i, dspl in enumerate(self.dspl):
            self.dspl[i] = wx.StaticText(self.panel, label="")

        self.history = wx.StaticText(self.panel, label="history:")
        self.HeightTop = wx.StaticText(self.panel, label="height top:")
        self.HeightBottom = wx.StaticText(self.panel, label="height bottom:")
        self.Width = wx.StaticText(self.panel, label="width:")
        self.Depth = wx.StaticText(self.panel, label="depth:")
        self.id = wx.StaticText(self.panel, label="id: " + (str(self.previous)))
        
        
        self.back = [0] * 4
        for i, back in enumerate(self.back):
            self.back[i] = wx.StaticText(self.panel, label="")
        
        #sizer setup
        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(self.panel, 1, wx.ALL | wx.EXPAND)  
        self.sizer = wx.GridBagSizer(5, 5)
        self.sizer.Add(self.ButtonSize7, (0,0))
        self.sizer.Add(self.ButtonSize10, (0,1))
        self.sizer.Add(self.id, (1,2))
        self.sizer.Add(self.history, (1,0))
        self.sizer.Add(self.HeightTop, (2,0))
        self.sizer.Add(self.HeightBottom, (3,0))
        self.sizer.Add(self.Depth, (4,0))
        self.sizer.Add(self.Width, (5,0))
        self.sizer.Add(self.prev_button,(6,2))
        self.sizer.Add(self.next_button,(6,3))
        for i, input in enumerate(self.back):
            self.sizer.Add(input,(i+2,2))
        fileDir = "fcc/data/BackLog.json"
        data = get_data(fileDir)
        
        
        self.previous -= 1
        self.id.SetLabel("id: " + (str(self.previous + 1)))
        calculations = data['calculations']

        values = calculations[self.previous]['Values']
        p_type = calculations[self.previous]['ProfileType']

        if p_type == "7mm":
            self.ButtonSize7.SetValue(True)
        else:
            self.ButtonSize10.SetValue(True)

        answer = [0] * 4
        for i, value in enumerate(values):
            answer[i] = values[i] + self.math[p_type][i]

        for i, back in enumerate(self.back):
            if answer[i] > 0:
                self.back[i].SetForegroundColour(wx.WHITE)
                self.back[i].SetLabel(str(answer[i]))
            else:
                self.back[i].SetForegroundColour(wx.RED)
                self.back[i].SetLabel(str(answer[i]))
        #button binding
        self.Bind(wx.EVT_BUTTON, self.on_show_prev, self.prev_button)
        self.Bind(wx.EVT_BUTTON, self.on_show_next, self.next_button)
        self.ButtonSize7.Bind(wx.EVT_RADIOBUTTON, self.on_radio_select)
        self.ButtonSize10.Bind(wx.EVT_RADIOBUTTON, self.on_radio_select)

        #border for sizer
        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, 1, wx.ALL | wx.EXPAND, 5)
        
        
        #Use the sizers
        self.panel.SetSizerAndFit(self.border)  
        self.SetSizerAndFit(self.windowSizer)

        #change number when radio change
    def on_radio_select(self, event):
        fileDir = "fcc/data/BackLog.json"
        data = get_data(fileDir)
        radio_button = event.GetEventObject()
        calculations = data['calculations']
        values = calculations[self.previous]['Values']
        p_type = radio_button.GetLabel()

        self.answer = [0] * 4
        for i, value in enumerate(values):
            self.answer[i] = values[i] + self.math[p_type][i]
                
        for i, back in enumerate(self.back):
            if self.answer[i] > 0:
                self.back[i].SetForegroundColour(wx.WHITE)
                self.back[i].SetLabel(str(self.answer[i]))
            else:
                self.back[i].SetForegroundColour(wx.RED)
                self.back[i].SetLabel(str(self.answer[i]))
            

        #function previus button
    def on_show_prev(self, e):
        fileDir = "fcc/data/BackLog.json"
        data = get_data(fileDir)
        
        if self.previous > 0:
            self.previous -= 1
            self.id.SetLabel("id: " + (str(self.previous + 1)))
            calculations = data['calculations']
            p_type = calculations[self.previous]['ProfileType']
            values = calculations[self.previous]['Values']
            
            self.answer = [0] * 4
            for i, value in enumerate(values):
                self.answer[i] = values[i] + self.math[p_type][i]
            if p_type == "7mm":
                self.ButtonSize7.SetValue(True)
            else:
                self.ButtonSize10.SetValue(True)
            
            for i, back in enumerate(self.back):
                if self.answer[i] > 0:
                    self.back[i].SetForegroundColour(wx.WHITE)
                    self.back[i].SetLabel(str(self.answer[i]))
                else:
                    self.back[i].SetForegroundColour(wx.RED)
                    self.back[i].SetLabel(str(self.answer[i]))

        #function next button
    def on_show_next(self, e):
        fileDir = "fcc/data/BackLog.json"
        data = get_data(fileDir)
        calculations = data['calculations']
        
        if self.previous < len(calculations) - 1:
            self.previous += 1
            self.id.SetLabel("id: " + (str(self.previous + 1)))
            p_type = calculations[self.previous]['ProfileType']
            values = calculations[self.previous]['Values']
            self.answer = [0] * 4
            for i, value in enumerate(values):
                self.answer[i] = values[i] + self.math[p_type][i]
            if p_type == "7mm":
                self.ButtonSize7.SetValue(True)
            else:
                self.ButtonSize10.SetValue(True)
            
            for i, back in enumerate(self.back):
                if self.answer[i] > 0:
                    self.back[i].SetForegroundColour(wx.WHITE)
                    self.back[i].SetLabel(str(self.answer[i]))
                else:
                    self.back[i].SetForegroundColour(wx.RED)
                    self.back[i].SetLabel(str(self.answer[i]))
        
        
#-------------------------------------------------------------------------------#

class DrawingFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="render", pos=wx.DefaultPosition, size=(512, 394),style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Centre()
        self.Show()
        fileDir = "fcc/data/BackLog.json"
        self.data = get_data(fileDir)
        self.calculations = self.data['calculations']
        self.previous = len(self.data['calculations'])
        self.previous =- 1
        values = self.calculations[self.previous]['Values']
        self.p_type = self.calculations[self.previous]['ProfileType']

        self.p_top =  values[0]     #top
        self.p_bottom = values[1]   #bottom
        self.p_side = values[2]     #depth
        self.p_front = values[3]     #width
        self.avg = (self.p_side + self.p_front/2)
        self.avg_b = (self.p_side + self.p_front + self.p_bottom /4)

       


    def calculate_scale(self):
        max_value = (self.avg)
        return 200 / max_value  
     
    
    def draw_line(self, dc, length, angle, line_width):
        """Draw a line in the direction of the angle for a certain length."""
        x, y = self.start_x, self.start_y
        corrected_angle = 360 - angle
        rad_angle = math.radians(corrected_angle)
        end_x = x + length * math.cos(rad_angle)
        end_y = y + length * math.sin(rad_angle)
        pen = wx.Pen(wx.WHITE, int(line_width))
        dc.SetPen(pen)
        dc.DrawLine(int(x), int(y), int(end_x), int(end_y))
        self.start_x, self.start_y = end_x, end_y

    def on_paint(self, event):
        dc = wx.ClientDC(self)
        gc = wx.GraphicsContext.Create(dc)

        # Calculate the dynamic scale factor
        scale_factor = self.calculate_scale()

        # Set the logical scale based on the scale factor
        dc.SetLogicalScale(scale_factor, scale_factor)

        # Calculate the starting position
        self.start_x = (self.p_side / 1)
        self.start_y = (self.avg_b * 0.9 )

        line_thickness = 2 / scale_factor  # Scale the line thickness inversely

        # Set the pen color to white
        gc.SetPen(wx.Pen(wx.WHITE, int(line_thickness)))

     # Drawing the shape using setheading angles
        self.draw_line(dc, self.p_bottom, 90, line_thickness)
        self.draw_line(dc, self.p_side, 320, line_thickness)
        self.draw_line(dc, self.p_bottom, 270, line_thickness)
        self.draw_line(dc, self.p_side, 140, line_thickness)
        self.draw_line(dc, self.p_front, 10, line_thickness)
        self.draw_line(dc, self.p_bottom, 90, line_thickness)
        self.draw_line(dc, self.p_side, 320, line_thickness)
        self.draw_line(dc, self.p_bottom, 270, line_thickness)
        self.draw_line(dc, self.p_side, 140, line_thickness)
        self.draw_line(dc, self.p_side, 320, line_thickness)
        self.draw_line(dc, self.p_front, 190, line_thickness)
        self.draw_line(dc, self.p_bottom, 90, line_thickness)
        self.draw_line(dc, self.p_front, 10, line_thickness)
        self.draw_line(dc, self.p_side, 140, line_thickness)
        self.draw_line(dc, self.p_front, 190, line_thickness)
        self.draw_line(dc, self.p_top, 115, line_thickness)
        self.draw_line(dc, self.p_front, 10, line_thickness)
        self.draw_line(dc, self.p_top, 295, line_thickness)
        self.draw_line(dc, self.p_side, 45, line_thickness)
        self.draw_line(dc, self.p_top, 115, line_thickness)
        self.draw_line(dc, -self.p_side, 45, line_thickness)
        self.draw_line(dc, -self.p_front, 10, line_thickness)
        self.draw_line(dc, self.p_side, 45, line_thickness)
        self.draw_line(dc, -self.p_top, 115, line_thickness)
        self.draw_line(dc, -self.p_side, 45, line_thickness)
        self.draw_line(dc, self.p_side, 45, line_thickness)
        self.draw_line(dc, self.p_front, 10, line_thickness)
        self.draw_line(dc, self.p_top, 115, line_thickness)
        self.draw_line(dc, -self.p_front, 10, line_thickness)
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

    return data
        
def write_data(fileDir, data):
    with open(fileDir, "w") as json_file:
        json.dump(data, json_file, indent=4)

#run program
if __name__ == "__main__":
    app = wx.App()
    frame = bucky(None, style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
    # frame.SetMaxSize((256, 197))
    frame.Show()
    app.MainLoop()
    

