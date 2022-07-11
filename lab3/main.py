import pygame as pg
import os, sys

from algoritmos.lineas.bresenham import bresenham
from algoritmos.cohen_sutherland import cohenSutherlandClip
from algoritmos.cyrus_beck import CyrusBeckClip
from algoritmos.sutherland_hodgman import sutherland_hodgman

# Defining x_max, y_max and x_min, y_min for rectangle
# Since diagonal points are enough to define a rectangle
x_max = 10.0
y_max = 8.0
x_min = 4.0
y_min = 4.0

n = 480 #matriz nxn, 480 -> 1:1 pixel
ancho = 720 #ancho de la pantalla
alto = ancho
size = ancho // n #tamaño del lado de cada cuadrado
ticks = 3 #velocidad del reloj, mayor valor -> mayor velocidad.

colores = { "viewport": (150,150,150) }

# origen de coordenadas
x0 = 0
y0 = n-1

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

def pintar_poligono(puntos, color=(0,0,0)):
    for i in range(0, len(puntos)-1): # range(0,4*) 4, 5
        puntos_recta = bresenham(puntos[i], puntos[i+1])
        print("i:",i)
        pintar_linea(puntos_recta) # pendiente verificar 
    ultima_recta = bresenham(puntos[0], puntos[-1])
    pintar_linea(ultima_recta)
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

        #pintar el viewport
        pintar_viewport(viewport)
        pintar_linea(puntos)
        #pintar_linea(bresenham(P1,P2), (200,200,0))
        put_pixel(0, 0, (255,0,0)) #mostrar punto de origen relativo
        #pintar_poligono([[10,10], [20,10], [30, 20], [20, 30], [10, 30],[0,20]])
        #pintar_poligono(((0,0),(100,0),(50,100)))
        pol = [[100, 290], [100, 210], [275, 230], [150, 250], [275, 270], [100, 290]]
        pintar_poligono(pol)
        #grid() #mostrar la cuadrícula.
        #pantalla.fill((255,255,255))

        #pg.display.update()
        pg.display.flip() #actualizar el mundo para mostrar nuevos cambios.

""" Puntos de la EII y la ESD """
def definir_viewport_E():
    print("Ingrese los valores de la EII y la ESD del viewport")
    x1 = int(input("Ingrese x1"))
    y1 = int(input("Ingrese y1"))
    x2 = int(input("Ingrese x2"))
    y2 = int(input("Ingrese y2"))
    
    return [(x1,y1), (x2,y2)]

def definir_viewport_TBLR():
    top = int(input("Ingrese el valor para TOP: "))
    bottom = int(input("Ingrese el valor para BOTTOM: "))
    left = int(input("Ingrese el valor para LEFT: "))
    right = int(input("Ingrese el valor para RIGHT: "))

    return [(left,bottom), (left,top), (right,top), (right,bottom)]

def definir_viewport_puntos():
    print("Ingrese los valores de cada punto para el viewport (en el sentido del reloj)")
    x1 = int(input("Ingrese x1"))
    y1 = int(input("Ingrese y1"))
    x2 = int(input("Ingrese x2"))
    y2 = int(input("Ingrese y2"))
    x3 = int(input("Ingrese x3"))
    y3 = int(input("Ingrese y3"))
    x4 = int(input("Ingrese x4"))
    y4 = int(input("Ingrese y4"))

    return [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]

def ingresar_datos_recta():
    print("Ingrese los puntos inicial y final de la línea")
    x1 = int(input("Ingrese x1"))
    y1 = int(input("Ingrese y1"))
    x2 = int(input("Ingrese x2"))
    y2 = int(input("Ingrese y2"))

    return [(x1,y1),(x2,y2)]
    
def ingresar_datos_poligono():
    num_vertices = int(input("Ingrese el número de vértices del polígono: "))
    for i in range(vertices_poligono):
        vertices_poligono = []
        print(f"vértice {i}:")
        vertices_poligono.append(tuple(input("ingrese el valor de x: "), input("ingrese el valor de x: ")))
    

if __name__ == "__main__":
    # Inicio
    global P1, P2
    setup() #pantalla
    clock = pg.time.Clock() #reloj para manipular la velocidad de la ejecución.
    """ x_min = 3.0
    y_min = 2.0
    x_max = 7.0
    y_max = 6.0
    EII = [x_min, y_min]
    ESD = [x_max, y_max] """

    """ x1 = 5.0
    y1 = 0.0
    x2 = 6.0
    y2 = 4.0
    P1 = [x1,y1]
    P2 = [x2,y2] """

    """  puntos = bresenham(P1, P2)
    puntos_c_s = cohenSutherlandClip(P1, P2, EII, ESD)
    puntos_c_b = CyrusBeckClip(P1, P2, EII, ESD)
    print("resultado de c-s: ", puntos_c_s)
    print("resultado de c-b:", puntos_c_b)
    print("linea: ", puntos)
    viewport = [EII, ESD]
    i_0 = puntos.index(puntos_c_s[0])
    i_f = puntos.index(puntos_c_s[1]) """

    #print("puntos: ", puntos)
    x1 = 1
    y1 = 2
    x2 = 23
    y2 = 12
    vertices = [[5, 5], [20, 2], [16, 10], [10, 10]]
    puntos = CyrusBeckClip([x1,y1], [x2,y2], vertices_viewport=vertices)
    i_0 = puntos.index(puntos[0])
    i_f = puntos.index(puntos[1])
    print("i_0 = ", i_0)
    print("i_f = ", i_f)
    print("dentro: ", puntos[i_0:i_f+1])
    mostrar_juego(viewport, puntos[i_0:i_f+1]) #mostrar el juego en pantalla.

    """ tipo_recorte = int(input("Ingrese 1 para recorte de líneas o 2 para polígonos: "))
    tipo_viewport = int(input("Ingrese la forma en la que quiere ingresar el viewport: 1 para EEI y ESD y 2 para (TOP, BOTTOM, LEFT, RIGHT)"))
    if tipo_recorte == 1: # recorte de líneas
        pass
    else: # recorte de polígonos
        pass """