#import the turtle modules 
import turtle 

B = 480     #top
A = 650     #bottom
X = 2000   #side
Y = 4200     #front

size_X = (X * 3)
size_y = (Y * 3)
start_pos = (X * 2)


# Forming the window screen 
tut = turtle.Screen() 
tut.setup(width=500, height=500)

# tut.tracer(0)
tut.bgcolor('black')

# window title Turtle 
turtle.setworldcoordinates(-start_pos, -start_pos, size_y, size_X)
tut.title("Turtle") 
turt = turtle.Turtle() 
turt.speed(0)


# object color 
turt.color("white") 
tut = turtle.Screen()	
turt.hideturtle()

turt.setheading(90)	 
turt.forward(A) #bottom
turt.setheading(320)
turt.forward(X) #side
turt.setheading(270)
turt.forward(A) #bottom
turt.setheading(140)
turt.forward(X) #side

turt.setheading(10)

turt.forward(Y) #front
turt.setheading(90)	 
turt.forward(A) #bottom
turt.setheading(320)
turt.forward(X)
turt.setheading(270)
turt.forward(A) #bottom
turt.setheading(140)
turt.forward(X)

turt.setheading(320)
turt.forward(X) #side
turt.setheading(190)
turt.forward(Y) #front
turt.setheading(90)
turt.forward(A) #bottom
turt.setheading(10)
turt.forward(Y) #front

turt.setheading(140)
turt.forward(X) #side
turt.setheading(190)
turt.forward(Y) #front

turt.setheading(115)
turt.forward(B) #top
turt.setheading(10)
turt.forward(Y) #front
turt.setheading(295)
turt.forward(B) #top

turt.setheading(45)
turt.forward(X) #side
turt.setheading(115)
turt.forward(B) #top
turt.setheading(45)
turt.back(X) #side

turt.setheading(10)
turt.back(Y)

turt.setheading(45)
turt.forward(X) #side
turt.setheading(115)
turt.back(B) #top
turt.setheading(45)
turt.back(X) #side

turt.forward(X)

turt.setheading(10)
turt.forward(Y) #front
turt.setheading(115)
turt.forward(B) #top
turt.setheading(10)
turt.back(Y) #front
turtle.done()
