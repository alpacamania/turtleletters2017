import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        tur.setpos(40, 0)
        tur.pendown()
    elif letter == "B":
	    pass
    elif letter == "C":
	    pass
    elif letter == "D":
	    pass
    elif letter == "E":
	    pass
    elif letter == "F":
	    pass
    elif letter == "G":
	    pass		
    elif letter == "H":
        tur.setheading(0)
        tur.penup()
        tur.forward(5)
        tur.right(90)
        tur.forward(5)
        tur.pendown()
        tur.forward(50)
        tur.penup()
        tur.backward(25)
        tur.left(90)
        tur.pendown()
        tur.forward(30)
        tur.left(90)
        tur.backward(25)
        tur.forward(50)
        tur.penup()
        tur.forward(5)
        tur.right(90)
        tur.forward(5)
        tur.pendown()
    elif letter == "I":
	    pass
    elif letter == "J":
	    pass
    elif letter == "K":
	    pass
    elif letter == "L":
	    pass
    elif letter == "M":
	    pass
    elif letter == "N":
	    pass
    elif letter == "O":
	    pass
    elif letter == "P":
	    pass		
    elif letter == "Q":
	tur.setheading(0)
        tur.penup()
        tur.forward(5)
        tur.right(90)
        tur.forward(30)
        tur.pendown()
        tur.circle(15,360)
        tur.penup()
        tur.setheading(0)
        tur.forward(15)
        tur.pendown()
        tur.setheading(315)
        tur.forward(22)
        tur.penup()
        tur.setheading(0)
        tur.forward(4)
        tur.left(90)
        tur.forward(46)
        tur.setheading(0)
    elif letter == "R":
	    pass
    elif letter == "S":
	    pass
    elif letter == "T":
	    pass
    elif letter == "U":
	    pass
    elif letter == "V":
        tur.setheading(0)
        tur.penup()
        tur.forward(20)
        tur.right(90)
        tur.forward(60)
        tur.right(180)
        tur.pendown()
        tur.left(20)
        tur.forward(45)
        tur.backward(45)
        tur.right(40)
        tur.forward(45)
        tur.backward(45)
        tur.left(20)
        tur.penup()
        tur.forward(60)
        tur.right(90)
        tur.forward(20)
        tur.pendown()
    elif letter == "W":
	    pass
    elif letter == "X":
	    pass
    elif letter == "Y":
	    pass
    elif letter == "Z":
	    pass		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        turtleLetter("box",tur)

window = turtle.Screen()
tur = turtle.Turtle()
tur.speed(100)
turtleLetter("A",tur)
turtleLetter("H",tur)
turtleLetter("H",tur)
turtleLetter("H",tur)
turtleLetter("H",tur)
turtleLetter("H",tur)

window.exitonclick()
