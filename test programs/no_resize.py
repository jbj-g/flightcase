import wx

app = wx.App()
frame = wx.Frame(None, style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
frame.Show()
app.MainLoop()