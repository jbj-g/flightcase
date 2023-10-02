import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, wx.ID_ANY, "Main Window", size=(300, 150))
        panel = wx.Panel(self)
        
        # Create a button
        self.button = wx.Button(panel, wx.ID_ANY, "Show Data")
        self.Bind(wx.EVT_BUTTON, self.on_show_data, self.button)
        
        # Center the button on the panel
        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(self.button, 1, wx.ALIGN_CENTER | wx.ALL, 10)
        panel.SetSizerAndFit(box)
        
    def on_show_data(self, event):
        # Create a new window to display data
        data_window = DataWindow(self)
        data_window.Show()

class DataWindow(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, wx.ID_ANY, "Data Window", size=(200, 100))
        
        # Create a text control to display data
        self.text_ctrl = wx.TextCtrl(self, wx.ID_ANY, "Data here", style=wx.TE_READONLY | wx.TE_CENTER)
        
        # Center the text control in the window
        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(self.text_ctrl, 1, wx.EXPAND | wx.ALL, 10)
        self.SetSizerAndFit(box)

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
