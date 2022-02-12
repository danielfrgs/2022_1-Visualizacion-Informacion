#ILUSION OPTICA USANDO LINEAS NEGRAS Y ROJAS
import turtle

#Definimos los parámetros de las líneas:
def drawLine(xFrom, yFrom, xTo, yTo, color):
    global myLapiz
    
    #Alzar el lápiz
    myLapiz.penup()
    myLapiz.color(color)
    
    #Establecer el punto (x,y) de origen:
    myLapiz.goto(xFrom,yFrom)
    
    #Bajar el lápiz
    myLapiz.pendown()
    
    #Moverse al segundo punto
    myLapiz.goto(xTo,yTo)

myLapiz = turtle.Turtle()

#Forma del lapiz: flecha o tortuga (turtle)
myLapiz.shape("arrow")

#Velocidad del trazo de línea
myLapiz.speed(2)

#Crear varias líneas a partir de un solo punto de origen:
for i in range(20):
    drawLine(0,150,300,20*i + 150,"Black")
    drawLine(0,150,300,-20*i + 150,"Black")

#Dibujar un rectángulo de acuerdo a las siguientes coordenadas:
    # drawLine(xFrom,yFrom,xTo,yTo,"color")
    
drawLine(80,100,250,100,"red")
drawLine(250,100,250,200,"red")
drawLine(250,200,80,200,"red")
drawLine(80,200,80,100,"red")

turtle.done()

