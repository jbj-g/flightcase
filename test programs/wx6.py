import wx
import math

B = 480     #top
A = 650     #bottom
X = 2000    #side
Y = 3200    #front

class DrawingFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="wxPython Drawing", size=(512, 394))
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Centre()
        self.Show()

    def calculate_scale(self):
        # Calculate the scale factor based on the maximum of A, B, X, and Y
        max_value = max(A, B, X, Y)
        return 200 / max_value  # 100 is an arbitrary scale for drawing

    def draw_line(self, dc, length, angle, line_width):
        """Draw a line in the direction of the angle for a certain length."""
        x, y = self.start_x, self.start_y
        corrected_angle = 360 - angle
        rad_angle = math.radians(corrected_angle)
        end_x = x + length * math.cos(rad_angle)
        end_y = y + length * math.sin(rad_angle)
        pen = wx.Pen(wx.Colour(255, 255, 255), int(line_width))
        dc.SetPen(pen)
        dc.DrawLine(int(x), int(y), int(end_x), int(end_y))
        self.start_x, self.start_y = end_x, end_y

    def on_paint(self, event):
        dc = wx.ClientDC(self)
        gc = wx.GraphicsContext.Create(dc)

        # Calculate the dynamic scale factor
        scale_factor = self.calculate_scale()

        # Set the logical scale based on the scale factor
        dc.SetLogicalScale(scale_factor, scale_factor)

        # Calculate the line thickness based on the scale factor
        line_thickness = 2 #/ scale_factor  # Scale the line thickness inversely

        # Set the pen color to white
        gc.SetPen(wx.Pen(wx.WHITE, int(line_thickness)))

        # Calculate the starting position
        self.start_x = 0
        self.start_y = 0

        # Drawing the shape using setheading angles
        self.draw_line(dc, A, 90, line_thickness)
        self.draw_line(dc, X, 320, line_thickness)
        self.draw_line(dc, A, 270, line_thickness)
        self.draw_line(dc, X, 140, line_thickness)
        self.draw_line(dc, Y, 10, line_thickness)
        self.draw_line(dc, A, 90, line_thickness)
        self.draw_line(dc, X, 320, line_thickness)
        self.draw_line(dc, A, 270, line_thickness)
        self.draw_line(dc, X, 140, line_thickness)
        self.draw_line(dc, X, 320, line_thickness)
        self.draw_line(dc, Y, 190, line_thickness)
        self.draw_line(dc, A, 90, line_thickness)
        self.draw_line(dc, Y, 10, line_thickness)
        self.draw_line(dc, X, 140, line_thickness)
        self.draw_line(dc, Y, 190, line_thickness)
        self.draw_line(dc, B, 115, line_thickness)
        self.draw_line(dc, Y, 10, line_thickness)
        self.draw_line(dc, B, 295, line_thickness)
        self.draw_line(dc, X, 45, line_thickness)
        self.draw_line(dc, B, 115, line_thickness)
        self.draw_line(dc, -X, 45, line_thickness)
        self.draw_line(dc, -Y, 10, line_thickness)
        self.draw_line(dc, X, 45, line_thickness)
        self.draw_line(dc, -B, 115, line_thickness)
        self.draw_line(dc, -X, 45, line_thickness)
        self.draw_line(dc, X, 45, line_thickness)
        self.draw_line(dc, Y, 10, line_thickness)
        self.draw_line(dc, B, 115, line_thickness)
        self.draw_line(dc, -Y, 10, line_thickness)

if __name__ == "__main__":
    app = wx.App(False)
    frame = DrawingFrame()
    app.MainLoop()
