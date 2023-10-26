import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        super(MyFrame, self).__init__(parent, id, title)

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Create two radio buttons with custom values
        radio_button1 = wx.RadioButton(panel, label="Option 1", style=wx.RB_GROUP)
        radio_button2 = wx.RadioButton(panel, label="Option 2")

        # Bind functions to radio buttons
        radio_button1.Bind(wx.EVT_RADIOBUTTON, self.on_radio_select)
        radio_button2.Bind(wx.EVT_RADIOBUTTON, self.on_radio_select)

        # Add radio buttons to the sizer
        sizer.Add(radio_button1, 0, wx.ALL, 10)
        sizer.Add(radio_button2, 0, wx.ALL, 10)

        panel.SetSizer(sizer)

    def on_radio_select(self, event):
        radio_button = event.GetEventObject()
        if radio_button.GetValue():
            if radio_button.GetLabel() == "Option 1":
                # Execute code for Option 1
                print("Option 1 selected. Running code for Option 1.")
                # Add your code for Option 1 here
            elif radio_button.GetLabel() == "Option 2":
                # Execute code for Option 2
                print("Option 2 selected. Running code for Option 2.")
                # Add your code for Option 2 here

app = wx.App()
frame = MyFrame(None, wx.ID_ANY, "Radio Buttons Example")
frame.Show()
app.MainLoop()
