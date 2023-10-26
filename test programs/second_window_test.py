import wx

class FirstWindow(wx.Frame):
    def __init__(self, parent, id, title):
        super(FirstWindow, self).__init__(parent, id, title, size=(400, 300))
        self.panel = wx.Panel(self)
        self.second_window = None  # Initialize second_window as None

        # Create a button that opens the second window
        button = wx.Button(self.panel, label="Open Second Window")
        button.Bind(wx.EVT_BUTTON, self.open_second_window)

        # Bind the close event for the first window
        self.Bind(wx.EVT_CLOSE, self.on_close)

    def open_second_window(self, event):
        self.second_window = SecondWindow(self, wx.ID_ANY, "Second Window")
        self.second_window.Show()

    def on_close(self, event):
        # Close the second window if it's open
        if self.second_window:
            self.second_window.Hide()
        event.Skip()

class SecondWindow(wx.Frame):
    def __init__(self, parent, id, title):
        super(SecondWindow, self).__init__(parent, id, title, size=(400, 300))

app = wx.App()
first_window = FirstWindow(None, wx.ID_ANY, "Bucky")
first_window.Show()
app.MainLoop()
