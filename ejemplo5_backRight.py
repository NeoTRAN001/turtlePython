# Se puede hacer una referencia a una api por medio de as
import turtle as t #Carcar la api de turtle

t.setup (500,500) # Configurar el espacio de dibujo

t.shape("turtle") # Dar forma de una tortuga
t.color("green") # Dar color

def moveTurle (position, move):
    angle = 90

    if (move == 'l'):
        t.left(angle) # .left() Girar a la izquierda 90 grados
    elif (move == 'r'):
        t.right(angle) # Mover derecha
    elif (move == 'b'):
        t.backward(angle) # Mover atras

    print (t.pos()) # .pos() nos devuelve la position

    t.forward(position) # .forward() Moverse hacia delante una cantidad n de pixeles

def line(power = 0):
    if (power == 1):
        t.pendown() # Dibujar la linea
    else:
        t.penup() # No dibujar la linea

line()

moveTurle(100, 'l')
moveTurle(100, 'r')
moveTurle(50, 'b')
moveTurle(100, 'x')


t.done() # Poner abajo del todo
t.bye()  # un done-bye para cerrar las rutinas
