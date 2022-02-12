#Gráficas Turtle es una forma muy habitual de introducción a la programación. 
#Imagina una tortuga robot que empieza en las coordenadas (0,0) en un plano x-y. 
#Después se le indica que se mueva, por ejemplo, 100 pixeles hacia adelante, dibujando una línea mientras se mueve.
#Después se le indica que rote, por ejemplo, 90 grados en el lugar, en sentido horario o antihorario
#Al combinar estos comandos y otros similares, se pueden dibujar figuras intrincadas y formas.
import _tkinter
import turtle

#A partir de la posición (0,0) le indicamos que se mueva 200 pixeles hacia adelante.
turtle.forward(200)

#En el lugar donde se encuentra, le indicamos que rote 90° hacia la izquierda.
turtle.left(90)

#A partir de la posición actual, le indicamos que se mueva 50 pixeles hacia adelante.
turtle.forward(50)

#Ahora que haga una rotación de 90° hacia la izquierda
turtle.left(90)

#A partir de su ubicación actual, le indicamos que avance 200 pixeles hacia adelante.
turtle.forward(200)

#Ahora que realice una rotación de 90° hacia la izquierda (sentido antihorario)
turtle.left(90)

#Ahora se le indica que avance 50 pixeles hacia adelante, mientras dibuja una linea.
turtle.forward(50)

# En su posición actual que haga una rotación de 20° hacia la derecha       
turtle.right(20)

#Repetimos pasos anteriores a partir de la rotación anterior.
turtle.forward(200)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(50)
turtle.right(30)

#Repetimos pasos anteriores a partir de la rotación anterior.
turtle.forward(200)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(50)

turtle.done()