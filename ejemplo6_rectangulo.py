# Se puede hacer una referencia a una api por medio de as
import turtle as t #Carcar la api de turtle
t.setup (500,500) # Configurar el espacio de dibujo

t.shape("turtle") # Dar forma de una tortuga
t.color("green") # Dar color

def rectangulo (px, py, ancho, alto):
    t.penup()
    t.goto(px + ancho / 2, py + alto / 2) # goto() ir a un punto en especifico
    t.seth(180) # seth() definir un angulo en directo iniciando desde 0 grados = izquierda
    t.pendown()

    t.forward(ancho)
    t.left(90)
    t.forward(alto)
    t.left(90)
    t.forward(ancho)
    t.left(90)
    t.forward(alto)
    t.left(90)

rectangulo(0, 0, 400, 300)
rectangulo(0, 0, 300, 200)
rectangulo(0, 0, 200, 100)
rectangulo(0, 0, 100, 50)

t.done() # Poner abajo del todo
t.bye()  # un done-bye para cerrar las rutinas
