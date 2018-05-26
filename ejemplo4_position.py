# Se puede hacer una referencia a una api por medio de as
import turtle as t #Carcar la api de turtle

t.setup (500,500) # Configurar el espacio de dibujo

t.shape("turtle") # Dar forma de una tortuga
t.color("green") # Dar color

print (t.pos()) # .pos() nos devuelve la position

t.forward(230) # .forward() Moverse hacia delante una cantidad n de pixeles
t.left(90) # .left() Girar a la izquierda 90 grados
t.forward(230)
t.left(90) # .left() Girar a la izquierda 90 grados
t.forward(470)
t.left(90) # .left() Girar a la izquierda 90 grados
t.forward(440)
t.left(90) # .left() Girar a la izquierda 90 grados
t.forward(470)
t.left(90) # .left() Girar a la izquierda 90 grados
t.forward(450)

print (t.pos())

t.done() # Poner abajo del todo
t.bye()  # un done-bye para cerrar las rutinas
