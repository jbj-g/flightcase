iport wx

class Window(wx.Frame):
    def __init__(self, title):
        super().__init__(parent = None, title = title)
        self.panel = wx.Panel(self)

        text = wx.StaticText(self.panel, label= "Hello World", pos=(50, 50))
        button = wx.Button(self.panel, label = "Press Me", pos=(200, 50))
        rb = wx.RadioButton(self.panel, label = "Pizza", pos=(50, 120))
        cb = wx.ComboBox(self.panel, value = "Kittens", pos=(200, 120))

        self.Centre()
        self.Show()
               
app = wx.App()
window = Window("WxPython Tutorial")
app.MainLoop()
