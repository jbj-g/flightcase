import wx
import math

p_top = 65    #top
p_bottom = 400    #bottom
p_side = 400   #side
p_front = 600   #front

class DrawingFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="wxPython Drawing", size=(512, 394))
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Centre()
        self.Show()

    def calculate_scale(self):
        # Calculate the scale factor based on the maximum of p_bottom, p_top, p_side, and p_front
        max_value = (p_side /0.8) #max(p_bottom, p_top, p_side, p_front)
        # print(200 / max_value)
        return 200 / max_value  
    
    
    def draw_line(self, dc, length, angle, line_width):
        """Draw a line in the direction of the angle for a certain length."""
        x, y = self.start_x, self.start_y
        corrected_angle = 360 - angle
        rad_angle = math.radians(corrected_angle)
        end_x = x + length * math.cos(rad_angle)
        end_y = y + length * math.sin(rad_angle)
        pen = wx.Pen(wx.WHITE, int(line_width))
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

        # Calculate the starting position
        self.start_x = (p_side / 5)
        self.start_y = (p_side / 0.6)

        line_thickness = 2 / scale_factor  # Scale the line thickness inversely

        # Set the pen color to white
        gc.SetPen(wx.Pen(wx.WHITE, int(line_thickness)))

     # Drawing the shape using setheading angles
        self.draw_line(dc, p_bottom, 90, line_thickness)
        self.draw_line(dc, p_side, 320, line_thickness)
        self.draw_line(dc, p_bottom, 270, line_thickness)
        self.draw_line(dc, p_side, 140, line_thickness)
        self.draw_line(dc, p_front, 10, line_thickness)
        self.draw_line(dc, p_bottom, 90, line_thickness)
        self.draw_line(dc, p_side, 320, line_thickness)
        self.draw_line(dc, p_bottom, 270, line_thickness)
        self.draw_line(dc, p_side, 140, line_thickness)
        self.draw_line(dc, p_side, 320, line_thickness)
        self.draw_line(dc, p_front, 190, line_thickness)
        self.draw_line(dc, p_bottom, 90, line_thickness)
        self.draw_line(dc, p_front, 10, line_thickness)
        self.draw_line(dc, p_side, 140, line_thickness)
        self.draw_line(dc, p_front, 190, line_thickness)
        self.draw_line(dc, p_top, 115, line_thickness)
        self.draw_line(dc, p_front, 10, line_thickness)
        self.draw_line(dc, p_top, 295, line_thickness)
        self.draw_line(dc, p_side, 45, line_thickness)
        self.draw_line(dc, p_top, 115, line_thickness)
        self.draw_line(dc, -p_side, 45, line_thickness)
        self.draw_line(dc, -p_front, 10, line_thickness)
        self.draw_line(dc, p_side, 45, line_thickness)
        self.draw_line(dc, -p_top, 115, line_thickness)
        self.draw_line(dc, -p_side, 45, line_thickness)
        self.draw_line(dc, p_side, 45, line_thickness)
        self.draw_line(dc, p_front, 10, line_thickness)
        self.draw_line(dc, p_top, 115, line_thickness)
        self.draw_line(dc, -p_front, 10, line_thickness)

if __name__ == "__main__":
    app = wx.App(False)
    frame = DrawingFrame()
    app.MainLoop()
