#ILUSION OPTICA USANDO CIRCULOS
import turtle

#Definimos los parámetros del círculo 
def drawCircle(x, y, radius, color):
    global myLapiz
    myLapiz.setheading(0)
    
    #Alzar Lápiz
    myLapiz.penup()
    
    myLapiz.color(color)
    myLapiz.fillcolor(color)
    
    #Moverse al siguiente punto
    myLapiz.goto(x,y-radius)
    
    #Realizar figura
    myLapiz.begin_fill()
    myLapiz.circle(radius)
    myLapiz.end_fill()
    
    #Bajar Lápiz
    myLapiz.pendown()
    
myLapiz = turtle.Turtle()
myLapiz.shape("arrow")
myLapiz.speed(2)

#Se establecen las coordenadas del primer conjunto de circulos:
drawCircle(-90, 0, 20 , "purple")
drawCircle(-90, 70, 35, "black")
drawCircle(-90, -70, 35, "black")
drawCircle(-160, 0, 35, "black")
drawCircle(-20, 0, 35, "black")

#Se establecen las coordenadas del segundo conjunto de circulos:
drawCircle(80, 0, 20 , "purple")
drawCircle(80, 35, 10, "black")
drawCircle(80, -35, 10, "black")
drawCircle(115, 0, 10, "black")
drawCircle(45, 0, 10, "black")

turtle.done()