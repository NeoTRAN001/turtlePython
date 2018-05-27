# Se puede hacer una referencia a una api por medio de as
import turtle as t #Carcar la api de turtle
t.setup (500,500) # Configurar el espacio de dibujo

t.shape("turtle") # Dar forma de una tortuga
t.color("green") # Dar color

def ordenar():
    orden = t.textinput("Orden requerida",
                        "Movimientos: a w s d - Salir: e") # Caja de texto

    if orden == "d": t.seth(0)
    elif orden == "w": t.seth(90)
    elif orden == "a": t.seth(180)
    elif orden == "s": t.seth(270)
    elif orden == "e": t.bye() # Cerrar ventana
    else: return

    t.forward(50)

while True: # Para que pueda moverse turtle hasta ingresar la tecla - e -
    ordenar()

t.done() # Poner abajo del todo
t.bye()  # un done-bye para cerrar las rutinas
