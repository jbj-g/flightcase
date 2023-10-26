import wx
import math

B = 48     #top
A = 65     #bottom
X = 200    #side
Y = 320    #front

size_X = (X * 3)
size_y = (Y * 3)
start_pos = (X * 2)

class DrawingFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="wxPython Drawing", size=(512, 394))
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Centre()
        self.Show()

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
        dc.SetLogicalScale(0.5, 0.5)
        dc.SetLogicalOrigin(size_X, size_y)

        # Calculate the center of the screen
        screen_width, screen_height = self.GetSize()
        center_x = screen_width / 2
        center_y = screen_height / 2

        # Calculate the scaling factor based on X and Y
        scale_factor_x = X / 200
        scale_factor_y = Y / 320

        # Calculate the scaled dimensions for the square
        side_length = 100 * scale_factor_x
        top_legnth = 100 * scale_factor_y

        # Calculate the starting position
        self.start_x = center_x - (side_length / 2)
        self.start_y = center_y - (top_legnth / 2)

    
        # Set the pen color to white
        dc.SetPen(wx.Pen(wx.WHITE, 1, wx.SOLID))

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
