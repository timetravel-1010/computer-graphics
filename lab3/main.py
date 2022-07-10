import pygame as pg
import os, sys

from algoritmos.cohen_sutherland import cohenSutherlandClip
from algoritmos.lineas.bresenham import bresenham

# Defining x_max, y_max and x_min, y_min for rectangle
# Since diagonal points are enough to define a rectangle
x_max = 10.0
y_max = 8.0
x_min = 4.0
y_min = 4.0

n = 48#matriz nxn, 480 -> 1:1 pixel
ancho = 720 #ancho de la pantalla
alto = ancho
size = ancho // n #tamaño del lado de cada cuadrado
ticks = 3 #velocidad del reloj, mayor valor -> mayor velocidad.

colores = { "viewport": (150,150,150) }

# origen de coordenadas
x0 = 10
y0 = n-20

#configuración inicial de la pantalla
def setup():
    global pantalla 
    pg.init()
    pantalla = pg.display.set_mode((ancho, alto))
    pg.display.set_caption('Smart Robot')
    pantalla.fill((255,255,255)) 

""" crear la cuadrícula """
def grid():
    x = 0
    y = 0
    limite_horizontal = alto
    limite_vertical = ancho
    for l in range(n+1):
        pg.draw.line(pantalla, (0,0,0), (x,0), (x, limite_horizontal))
        pg.draw.line(pantalla, (0,0,0), (0,y), (limite_vertical, y))
        x += size
        y += size

def put_pixel(x, y, color=(0,0,0)):
    global size
    pg.draw.rect(pantalla, color, ((x0 + x)*size, (y0 - y)*size, size, size))

def pintar_viewport(viewport):
    x_min, y_min = viewport[0]
    x_max, y_max = viewport[1]

    bottom = bresenham([x_min, y_min], [x_max, y_min]) #linea inferior
    top = bresenham([x_min, y_max], [x_max, y_max]) #linea superior
    left = bresenham([x_min, y_min], [x_min, y_max]) #linea superior
    right = bresenham([x_max, y_min], [x_max, y_max]) #linea superior
    lineas = [bottom, top, left, right]

    for linea in lineas:
        pintar_linea(linea, (200,0,200))

def pintar_linea(puntos, color=(0,0,0)):
    for punto in puntos:
        put_pixel(punto[0], punto[1], color)

def pintar_cuadrado(inicio, size):
    x, y = inicio
    xf, yf = x+size, y+size

# bucle infinito para mostrar en patalla todos los elementos gráficos.
def mostrar_juego(viewport, puntos): 
    while True:
        clock.tick(ticks) 
        
        for event in pg.event.get():
            if event.type == pg.QUIT: #para detener la ejecución al cerrar la ventana
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    pass

        """ if (i >= 0):            
            try:
                pintar_mundo(resultado[i][1]) #pinta el mundo correspondiente al nodo actual.
                robot.mover(resultado[i][0]) #se obtiene el operador para mover el robot. 
                #print("combustible actual:", resultado[i][2])
                #print("costo: ", resultado[i][3])
                #print("heuristica: ", resultado[i][4])
                robot.pintar()
            except ValueError:
                print("No se encontró la solución.") """

        #pintar el viewport
        pintar_viewport(viewport)
        pintar_linea(puntos)
        #pintar_linea(bresenham(P1,P2), (200,200,0))
        put_pixel(0, 0, (255,0,0)) #mostrar punto de origen relativo
        """ for punto in puntos:
            put_pixel(punto[0], punto[1], (200,100,200)) """

        #grid() #mostrar la cuadrícula.
        #pantalla.fill((255,255,255))

        #pg.display.update()
        pg.display.flip() #actualizar el mundo para mostrar nuevos cambios.

if __name__ == "__main__":
    # Inicio
    global P1, P2
    setup() #pantalla
    clock = pg.time.Clock() #reloj para manipular la velocidad de la ejecución.
    puntos = []
    x_min = 3.0
    y_min = 2.0
    x_max = 7.0
    y_max = 6.0
    EII = [x_min, y_min]
    ESD = [x_max, y_max]

    x1 = 5.0
    y1 = 0.0
    x2 = 6.0
    y2 = 4.0
    P1 = [x1,y1]
    P2 = [x2,y2]

    puntos = bresenham(P1, P2)
    puntos_dentro = cohenSutherlandClip(P1, P2, EII, ESD)
    puntos_dentro = list(map(lambda punto: [int(punto[0]), int(punto[1])], puntos_dentro))
    print("resultado de c-s: ", puntos_dentro)
    print("linea: ", puntos)
    viewport = [EII, ESD]
    i_0 = puntos.index(puntos_dentro[0])
    i_f = puntos.index(puntos_dentro[1])
    print("i_0 = ", i_0)
    print("i_f = ", i_f)
    print("dentro: ", puntos[i_0:i_f+1])
    #print("puntos: ", puntos)
    mostrar_juego(viewport, puntos[i_0:i_f+1]) #mostrar el juego en pantalla.