import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title)
        self.Show()

        # Bind the EVT_FULLSCREEN event
        self.Bind(wx.EVT_FULLSCREEN, self.on_fullscreen)

    def on_fullscreen(self, event):
        event.Skip()
        self.ShowFullScreen(False, wx.FULLSCREEN_ALL)


app = wx.App(False)
frame = MyFrame(None, "Prevent Full Screen Example")
app.MainLoop()
