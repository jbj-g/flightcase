import wx
import wx.lib.intctrl

class NumberInputFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title="Number Input", pos=wx.DefaultPosition, size=(300, 150)):
        super(NumberInputFrame, self).__init__(parent, id, title, pos, size)

        panel = wx.Panel(self)

        # Create an IntCtrl widget
        self.number_input = wx.lib.intctrl.IntCtrl(panel, value=0, allow_none=False, allow_long=False)

        # Create a button to show the entered number
        show_button = wx.Button(panel, label="Show Number")
        show_button.Bind(wx.EVT_BUTTON, self.on_show_button_click)

        # Layout the widgets using a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(wx.StaticText(panel, label="Enter a Number:"), 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(self.number_input, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(show_button, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(sizer)

    def on_show_button_click(self, event):
        entered_number = self.number_input.GetValue()
        wx.MessageBox(f"You entered: {entered_number}", "Entered Number", wx.OK | wx.ICON_INFORMATION)

if __name__ == "__main__":
    app = wx.App()
    frame = NumberInputFrame(None)
    frame.Show()
    app.MainLoop()

