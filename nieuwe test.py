import wx

app = wx.App()
frame = wx.Frame(None, wx.ID_ANY, "GridSizer Example")

panel = wx.Panel(frame)
grid = wx.BoxSizer(rows=2, cols=2, vgap=10, hgap=10)

button1 = wx.Button(panel, label="Button 1")
button2 = wx.Button(panel, label="Button 2")
button3 = wx.Button(panel, label="Button 3")
button4 = wx.Button(panel, label="Button 4")

# Set the minimum size for each button to 60 pixels wide
button1.SetMaxSize((60, -1))
button2.SetMaxSize((60, -1))
button3.SetMaxSize((60, -1))
button4.SetMaxSize((60, -1))

grid.Add(button1, 0)
grid.Add(button2, 0)
grid.Add(button3, 0)
grid.Add(button4, 0)

panel.SetSizer(grid)
frame.Show()
app.MainLoop()
