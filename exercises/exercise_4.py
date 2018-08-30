import turtle
turtle = turtle.Turtle()
turtle.reset()

def drawShape(sides, sideLength):
    angle = 360/sides
    for x in range(0, sides):
        turtle.forward(sideLength)
        turtle.left(angle)

def drawSquare(sideLength):
    drawShape(4, sideLength)

def drawSquareWithFill(color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    drawSquare(100)
    turtle.end_fill()

def moveToRight(distance):    
    turtle.up()
    turtle.fd(distance)
    turtle.down()

def moveTurtle(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()    

#Part 1 - Drawing shapes
#Reposition
moveTurtle(-300, 0)
#execute
drawShape(6, 100)
drawShape(5, 100)
drawShape(4, 100)
drawShape(3, 100)

#Part 2 - Filling shapes
#Reposition
moveToRight(300)
turtle.left(45)
#execute
drawSquareWithFill('green')
turtle.right(45)
moveToRight(100)
turtle.left(45)
drawSquareWithFill('yellow')

#Part 3 - Side by side squares
#Reposition
moveTurtle(-300, -250)
turtle.right(45)
#execute
drawSquare(100)
moveToRight(100)
drawSquare(50)
moveToRight(50)
drawSquare(25)
moveToRight(25)

#Part 4 - 4 squares in one
#Reposition
moveToRight(100)
drawSquare(100)
moveToRight(100)
#execute
drawSquare(100)
moveToRight(100)
turtle.left(90)
turtle.fd(100)
drawSquare(100)
moveToRight(100)
turtle.left(90)
turtle.fd(100)
drawSquare(100)
moveToRight(100)
