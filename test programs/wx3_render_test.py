import wx
import math

B = 48     #top
A = 65     #bottom
X = 200    #side
Y = 320    #front

size_X = (X * 3)
size_Y = (Y * 3)
start_pos = (X * 2)


class DrawingFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="wxPython Drawing", size=(512, 394))
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Centre()
        self.Show()

    def draw_line(self, gc, length, angle):
        """Draw a line in the direction of the angle for a certain length."""
      
        x, y = (X * 1.5), (Y * 1.3)
        corrected_angle= 360 - angle
        rad_angle = math.radians(corrected_angle)
        end_x = x + length * math.cos(rad_angle)
        end_y = y + length * math.sin(rad_angle)
        gc.StrokeLine(x, y, end_x, end_y)
        gc.Translate(end_x - x, end_y - y)
        

    def on_paint(self, event):
        dc = wx.PaintDC(self)
        gc = wx.GraphicsContext.Create(dc)
        dc.SetLogicalScale(0.5, 0.5)  # Scale the drawing
        dc.SetLogicalOrigin(0, 0)

        # Set color and starting position
        gc.SetPen(wx.Pen("white", 2))
        
        
        # Drawing the shape using setheading angles
        self.draw_line(gc, A, 90)
        self.draw_line(gc, X, 320)
        self.draw_line(gc, A, 270)
        self.draw_line(gc, X, 140)
        self.draw_line(gc, Y, 10)
        self.draw_line(gc, A, 90)
        self.draw_line(gc, X, 320)
        self.draw_line(gc, A, 270)
        self.draw_line(gc, X, 140)
        self.draw_line(gc, X, 320)
        self.draw_line(gc, Y, 190)
        self.draw_line(gc, A, 90)
        self.draw_line(gc, Y, 10)
        self.draw_line(gc, X, 140)
        self.draw_line(gc, Y, 190)
        self.draw_line(gc, B, 115)
        self.draw_line(gc, Y, 10)
        self.draw_line(gc, B, 295)
        self.draw_line(gc, X, 45)
        self.draw_line(gc, B, 115)
        self.draw_line(gc, -X, 45)  # Negative value to draw in opposite direction
        self.draw_line(gc, -Y, 10)
        self.draw_line(gc, X, 45)
        self.draw_line(gc, -B, 115)
        self.draw_line(gc, -X, 45)
        self.draw_line(gc, X, 45)
        self.draw_line(gc, Y, 10)
        self.draw_line(gc, B, 115)
        self.draw_line(gc, -Y, 10)

if __name__ == "__main__":
    app = wx.App(False)
    frame = DrawingFrame()
    app.MainLoop()