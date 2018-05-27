# Se puede hacer una referencia a una api por medio de as
import turtle as t #Carcar la api de turtle
t.setup (500,500) # Configurar el espacio de dibujo

t.shape("turtle") # Dar forma de una tortuga
t.color("green") # Dar color

def move(angle, steps):
    t.seth(angle)
    t.forward(steps)
    
def salir(): t.bye()

def arriba():     move(90,20)
def abajo():      move(270,20)
def izquierda():  move(180,20)
def derecha():    move(0,20)
# Enlazar la function con una tecla
t.onkey(arriba, "w") # Arriba
t.onkey(abajo, "s") # Abajo
t.onkey(izquierda, "a") # Izquierda
t.onkey(derecha, "d") # Derecha


# Turtle listener actions
t.listen()

t.done() # Poner abajo del todo
t.bye()  # un done-bye para cerrar las rutinas
