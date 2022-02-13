import turtle as ts

# Vammos a definnir el color del fonndo
#ts.bgcolor("grey")

# Vamos a definir una función que dibuje cuadrados

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

col = ['#a9cce3',
        '#7fb3d5',
        '#5499c7',
       '#2980b9',
        '#2471a3',
        '#1f618d',
        '#1a5276',
        '#154360']

mylapiz = ts.Turtle()

for x in range(0, 401, 10):
    draw_line(x, 400, 400, 400 - x, 'black')

for x in range(0, 401, 10):
    draw_line(-x, 400, -400, 400 - x, 'black')

for x in range(0, 401, 10):
    draw_line(400, x - 400, x, -400, 'black')

for x in range(0, 401, 10):
    draw_line(-400, x - 400, -x, -400, 'black')


# ESTRELLA

for x in range(0, 401, 10):
    draw_line(x, 0, 0, 400 - x, 'black')

for x in range(0, 401, 10):
    draw_line(-x, 0, 0, -400 + x, 'black')

for x in range(0, 401, 10):
    draw_line(-x, 0, 0, 400 - x, 'black')

for x in range(0, 401, 10):
    draw_line(x, 0, 0, -400 + x, 'black')

ts.getscreen()
#ts.done()
# Guardar
ts.getcanvas().postscript(file="Tareas/T2/t2_b.eps")

