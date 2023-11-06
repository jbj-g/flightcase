import wx

class bucky(wx.Frame):
    
    def __init__(self, parent, id):
        global panel
        global button
        #frame en panel
        wx.Frame.__init__(self, parent, id,'Flingtcase calculator', size = (600, 400))
        panel = wx.Panel(self)

        #menu bar
        MenuBar = wx.MenuBar()
        FirstMenu = wx.Menu()
        SecondMenu = wx.Menu()
        FirstMenu.Append(wx.NewId(), "New Window", "create a new window")
        FirstMenu.Append(wx.NewId(), "open...", "create a new window")
        MenuBar.Append(FirstMenu, "File")
        MenuBar.Append(SecondMenu, "Edit")
        self.SetMenuBar(MenuBar)
        
        self.sizer = wx.GridBagSizer(5, 5)
        #status bar en menu 
        status = self.CreateStatusBar()  

        #exit button
        button = wx.Button(panel, label = "exit", pos=(500,300), size = (60,60))
        self.Bind(wx.EVT_BUTTON, self.CloseButton, button)
        self.Bind(wx.EVT_CLOSE, self.CloseWindow)
        
        #exit button functies
    def CloseButton(self, event):
        self.Close(True)

        #save button functies
    def OnButton(self, e):
        self.result.SetLabel(self.input1.GetValue())
    def CloseWindow(self, event):
        self.Destroy()
        

if __name__ == "__main__":
    app = wx.App()
    frame = bucky  (parent = None, id = -1)
    frame.SetMinSize(wx.Size(320,240))
    def size_change(event):
        width,height = event.GetSize()
        width = int(width)
        height = int(height)
        panel.SetSize(width, height)
        print("x:",width)
        print("y:",height)
        button.Move(wx.Point(width-100,height-100))
    frame.Bind(wx.EVT_SIZE, size_change)    
    frame.Show()
    app.MainLoop()