# IMAGEN 2
# Vamos a crear la primera image de la Tarea 2

import turtle as ts

# Tamaño del canva
ts.setup(840,440)

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

def draw_square(x, y, size, color):
    global mylapiz
    # Definimos la orientación
    mylapiz.setheading(0)
    
    #Alzar lápiz
    mylapiz.penup()
    mylapiz.goto(x,y)
    mylapiz.color(color)
    mylapiz.fillcolor(color)    
    
    #Bajar lápiz
    mylapiz.pendown()
    
    #Rellenar la figura del color:
    mylapiz.begin_fill()
    mylapiz.forward(size)
    mylapiz.left(90)
    mylapiz.forward(size)
    mylapiz.left(90)
    mylapiz.forward(size)
    mylapiz.left(90)
    mylapiz.forward(size)
    mylapiz.end_fill()

# Vamos a definir una función que genere circulos

def draw_circle(x, y, radius, color):
    global mylapiz
    mylapiz.setheading(0)
    
    #Alzar Lápiz
    mylapiz.penup()
    
    mylapiz.color(color)
    mylapiz.fillcolor(color)
    
    #Moverse al siguiente punto
    mylapiz.goto(x,y-radius)
    
    #Realizar figura
    mylapiz.begin_fill()
    mylapiz.circle(radius)
    mylapiz.end_fill()
    
    #Bajar Lápiz
    mylapiz.pendown()

mylapiz = ts.Turtle()

# Vamos a definir una función para rectangulos

def draw_rectangule(x_i, y_i, size_a, size_b, color):
    global mylapiz
    # Definimos la orientación
    mylapiz.setheading(0)
    
    #Alzar lápiz
    mylapiz.penup()
    mylapiz.goto(x_i,y_i)
    mylapiz.color(color)
    mylapiz.fillcolor(color)    
    
    #Bajar lápiz
    mylapiz.pendown()
    
    #Rellenar la figura del color:
    mylapiz.begin_fill()
    mylapiz.forward(size_a)
    mylapiz.left(90)
    mylapiz.forward(size_b)
    mylapiz.left(90)
    mylapiz.forward(size_a)
    mylapiz.left(90)
    mylapiz.forward(size_b)
    mylapiz.end_fill()

# rectangulo inicial

draw_rectangule(-420, -220, 830, 430, 'grey')

# Vamos areducir 10px de cada lado para generar una margen

for x in range(-400, 400, 80):
    for y in range(-200, 200, 80):
        # El cuadrado que queremos dibujar será mñas chico para obtener una margen de 10 px
        draw_square(x, y, 70, 'black')

# Generaremos los circulos

for x in range(-325, 320, 80):
    for y in range(-125, 120, 80):
        draw_circle(x, y, 10, 'white')

ts.end_fill()
#ts.done()
# Guardar
ts.getcanvas().postscript(file="Tareas/T2/t2_b_1.eps")