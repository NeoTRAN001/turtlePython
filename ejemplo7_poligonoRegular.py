# Se puede hacer una referencia a una api por medio de as
import turtle as t #Carcar la api de turtle
t.setup (800,800) # Configurar el espacio de dibujo

t.shape("turtle") # Dar forma de una tortuga
t.color("green") # Dar color

def pen(power = 0):
    if (power == 1):
        t.pendown() # Dibujar la linea
    else:
        t.penup() # No dibujar la linea

def poligonoRegular(px, py, radio, lados):
    pen(0)
    t.goto(px, py - radio)
    pen(1)
    t.circle(radio) # Crear una circunferencia

    angle =  360 / lados
    vertices = []

    for i in range(lados):
        print(t.pos())
        pen(0)
        t.goto(px, py) # Estar en el centro del poligono
        pen(1)

        t.seth(angle*i+1) # Trazar radios hacia afuera
        t.forward(radio)
        vertices.append(t.pos()) # Agregar la position al arreglo

    # Iniciar desde la ultima position
    pen(0)
    t.goto(vertices[-1])
    pen(1)
    t.color("red")
    # Ahora la turtle se movera en cada uno de ellos
    for i in vertices:
        t.goto(i)

    t.color("green")

def option():
    n = int(input("Write a number: "))
    if(n == 1):
        for i in range(15):
            print(t.pos())
            poligonoRegular(0, 0, 400 / 2, 15 - i)
    elif(n == 2):
        for n in range(3, 21):
            poligonoRegular(0, 0, n*10, n)
    else:
        for i in range(2, 13):
            poligonoRegular(i * 10, 0, 400 / 2, 14 - i)

t.speed(100)

option()

t.done() # Poner abajo del todo
t.bye()  # un done-bye para cerrar las rutinas
