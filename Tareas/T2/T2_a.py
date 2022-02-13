# IMAGEN 1
# Vamos a crear la primera image de la Tarea 2

# Priemro Vamos a definir una función tal como hicimos en la práctica que nos dibuje una linea

import turtle as ts

def draw_line(xFrom, yFrom, xTo, yTo, color, size = 1):
    # Definimos la variable global
    global mylapiz

    # Grueso de la línea
    mylapiz.pensize(size)
    # Alzar el lápiz
    mylapiz.penup() 
    # Definir color 
    mylapiz.color(color)

    #Establecer el punto (x,y) de origen:
    mylapiz.goto(xFrom,yFrom)
    
    #Bajar el lápiz
    mylapiz.pendown()
    
    #Moverse al segundo punto
    mylapiz.goto(xTo,yTo)

# Vamos a ddefinir a 'Mylapiz' como un objeto de la clase Turtle 
mylapiz = ts.Turtle()

# Vamos a crear un ciclo que nos permita crear varias veces una linea

for x in range(-400, 400, 50):
    draw_line(x, 200, -x, -200, 'black')

for y in [-100, 100]:
    draw_line(400, y, -400, y, 'purple', size = 3)


ts.getscreen()
#ts.done()
# Guardar
ts.getcanvas().postscript(file="Tareas/T2/t2_a.eps")