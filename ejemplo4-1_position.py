# Se puede hacer una referencia a una api por medio de as
import turtle as t #Carcar la api de turtle

t.setup (500,500) # Configurar el espacio de dibujo

t.shape("turtle") # Dar forma de una tortuga
t.color("green") # Dar color

def createPosition (position):
    t.forward(position) # .forward() Moverse hacia delante una cantidad n de pixeles
    t.left(90) # .left() Girar a la izquierda 90 grados
    print (t.pos()) # .pos() nos devuelve la position

createPosition(230)
createPosition(230)
createPosition(470)
createPosition(440)
createPosition(470)
createPosition(250)

t.done() # Poner abajo del todo
t.bye()  # un done-bye para cerrar las rutinas
