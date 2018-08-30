import math
import turtle
turtle = turtle.Turtle()
turtle.reset()

def irParaDireita(distancia):    
    turtle.up()
    turtle.fd(distancia)
    turtle.down()
    
def moverTurtle(turtle, x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()    

def desTrianRet(turtle, tamanhoCateto):
    turtle.forward(tamanhoCateto)
    turtle.left(90)
    turtle.forward(tamanhoCateto)
    turtle.left(135)
    #Pitágoras
    hipotenusa = math.sqrt(tamanhoCateto ** 2 + tamanhoCateto ** 2)
    turtle.forward(hipotenusa)

def desTrianRetPreenchido(turtle, tamanhoCateto, cor):
    turtle.fillcolor(cor)
    turtle.begin_fill()
    desTrianRet(turtle, tamanhoCateto)
    turtle.end_fill()
    
def desLinha(turtle, tamanho, cor, espessura):
    turtle.width(espessura)
    turtle.color(cor)
    turtle.fd(tamanho)

def desCirculo(turtle, raio, x, y, cor, espessura):
    moverTurtle(turtle, x, y)
    turtle.width(espessura)
    turtle.color(cor)
    turtle.circle(raio)

def desCirculoPreenchido(turtle, raio, x, y, cor, espessura):
    turtle.fillcolor(cor)
    turtle.begin_fill()
    desCirculo(turtle, raio, x, y, cor, espessura)
    turtle.end_fill()

#1.1
moverTurtle(turtle, -300, 0)
desTrianRet(turtle, 200)

#1.2
turtle.left(90)
irParaDireita(100)
desTrianRetPreenchido(turtle, 200, 'red')

#1.3
turtle.left(180)
irParaDireita(400)
desLinha(turtle, 100, 'green', 10)

#1.4
turtle.left(180)
irParaDireita(400)
desCirculo(turtle, 100, 0, 0, 'blue', 10)

#1.4
turtle.left(180)
irParaDireita(400)
desCirculoPreenchido(turtle, 100, 0, 0, 'blue', 10)
