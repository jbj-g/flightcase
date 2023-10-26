import wx
import math

B = 48    #top
A = 65     #bottom
X = 200   #side
Y = 320   #front

class DrawingFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="wxPython Drawing", size=(512, 394))
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Centre()
        self.Show()

    def calculate_scale(self):
        # Calculate the scale factor based on the maximum of A, B, X, and Y
        max_value = (X/0.8) #max(A, B, X, Y)
        return 200 / max_value  
    def draw_line(self, dc, length, angle):
        """Draw a line in the direction of the angle for a certain length."""
        x, y = self.start_x, self.start_y
        corrected_angle = 360 - angle
        rad_angle = math.radians(corrected_angle)
        end_x = x + length * math.cos(rad_angle)
        end_y = y + length * math.sin(rad_angle)
        dc.DrawLine(int(x), int(y), int(end_x), int(end_y))
        self.start_x, self.start_y = end_x, end_y

    def on_paint(self, event):
        dc = wx.ClientDC(self)
        gc = wx.GraphicsContext.Create(dc)

        # Calculate the dynamic scale factor
        scale_factor = self.calculate_scale()

        # Set the logical scale based on the scale factor
        dc.SetLogicalScale(scale_factor, scale_factor)

        # Set the pen color to white
        dc.SetPen(wx.Pen(wx.WHITE, 1, wx.SOLID))

        # Calculate the starting position
        self.start_x = (X / 5)
        self.start_y = (X / 0.6)

        # Drawing the shape using setheading angles
        self.draw_line(dc, A, 90)
        self.draw_line(dc, X, 320)
        self.draw_line(dc, A, 270)
        self.draw_line(dc, X, 140)
        self.draw_line(dc, Y, 10)
        self.draw_line(dc, A, 90)
        self.draw_line(dc, X, 320)
        self.draw_line(dc, A, 270)
        self.draw_line(dc, X, 140)
        self.draw_line(dc, X, 320)
        self.draw_line(dc, Y, 190)
        self.draw_line(dc, A, 90)
        self.draw_line(dc, Y, 10)
        self.draw_line(dc, X, 140)
        self.draw_line(dc, Y, 190)
        self.draw_line(dc, B, 115)
        self.draw_line(dc, Y, 10)
        self.draw_line(dc, B, 295)
        self.draw_line(dc, X, 45)
        self.draw_line(dc, B, 115)
        self.draw_line(dc, -X, 45)
        self.draw_line(dc, -Y, 10)
        self.draw_line(dc, X, 45)
        self.draw_line(dc, -B, 115)
        self.draw_line(dc, -X, 45)
        self.draw_line(dc, X, 45)
        self.draw_line(dc, Y, 10)
        self.draw_line(dc, B, 115)
        self.draw_line(dc, -Y, 10)

if __name__ == "__main__":
    app = wx.App(False)
    frame = DrawingFrame()
    app.MainLoop()
