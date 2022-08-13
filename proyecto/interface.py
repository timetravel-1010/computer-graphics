import pygame as pg
import os, sys

from algoritmos.rastering.bresenham import bresenham
""" from algoritmos.cohen_sutherland import cohenSutherlandClip
from algoritmos.cyrus_beck import CyrusBeckClip
from algoritmos.sutherland_hodgman import PolygonClipper
from algoritmos.weiler_atherton import weilerAthertonClip """

# Defining x_max, y_max and x_min, y_min for rectangle
# Since diagonal points are enough to define a rectangle
""" x_max = 10.0
y_max = 8.0
x_min = 4.0
y_min = 4.0 """

n = 480 #matriz nxn, 480 -> 1:1 pixel
ancho = 720 #ancho de la pantalla
alto = ancho
size = ancho // n #tamaño del lado de cada *pixel*

normal_size = ancho // 10 #10 -> número de columnas y filas
print("size:" , size)

# origen de coordenadas, cambiar en caso de necesitar
x0 = 0
y0 = 0

#configuración inicial de la pantalla
def setup():
    global pantalla 
    pg.init()
    pantalla = pg.display.set_mode((ancho, alto))
    pg.display.set_caption('Smart RobotUI')
    pantalla.fill((255,255,255)) 

def input():
    global x0, y0, pos_item1, pos_item2
    items_encontrados = 0

    with open(f"mundos/{nombre_lectura}.txt", "r") as f:
        content = f.read().split('\n')
        mundo = []
        for i in range(n):
            fila = list(map(lambda x: int(x), content[i].split(" ")))
            mundo.append(fila)
            try: 
                y0 = fila.index(2)
                x0 = i  
            except ValueError:
                pass 
            try:
                if items_encontrados == 0:
                    y = fila.index(5)
                    pos_item1['y'] = y  # [0 1 1 1 1 0 1 1 1 5]-> 9
                    pos_item1['x'] = i
                    items_encontrados += 1 
                    try: 
                        pos_item2['y'] = fila.index(5, y+1) # [0 1 1 1 1 0 1 1 1 5]-> 9
                        pos_item2['x'] = i
                        items_encontrados += 1
                    except ValueError:
                        pass 
                elif items_encontrados == 1:
                    pos_item2['y'] = fila.index(5) # [0 1 1 1 1 0 1 1 1 5]-> 9
                    pos_item2['x'] = i
                    items_encontrados += 1  
            except ValueError:
                pass
        return np.array(mundo)

""" crear la cuadrícula """
def grid():
    x = 0
    y = 0
    limite_horizontal = alto
    limite_vertical = ancho
    for l in range(n+1):
        pintar_linea(bresenham((x,0), (x, limite_horizontal)), color=(0,0,0))
        pintar_linea(bresenham((0,y), (limite_vertical, y)), color=(0,0,0))
        x += normal_size
        y += normal_size

""" 
función que permite el dibujo de un rectángulo que actúa como unidad fundamental, el pixel.
"""
def put_pixel(x, y, color=(0,0,0)):
    global size
    pg.draw.rect(pantalla, color, (x*size, y*size, size, size))

def pintar_viewport_TBLR(TOP, BOTTOM, LEFT, RIGHT, color=(255,0,0)):
    
    top = bresenham([LEFT, TOP], [RIGHT, TOP]) #linea superior
    bottom = bresenham([LEFT, BOTTOM], [RIGHT, BOTTOM]) #linea inferior
    left = bresenham([LEFT, BOTTOM], [LEFT, TOP]) #linea de la izquierda
    right = bresenham([RIGHT, BOTTOM], [RIGHT, TOP]) #linea de la derecha
    lineas = [bottom, top, left, right]

    for linea in lineas:
        pintar_linea(linea, color=(255,0,0))

def pintar_viewport_vertices(vertices, color=(255,0,0)):
    pintar_poligono(vertices, color=color)

def pintar_viewport_E(EII, ESD):
    
    x_min, y_min = EII
    x_max, y_max = ESD
    
    top = bresenham([x_min, y_max], [x_max, y_max]) #linea superior
    bottom = bresenham([x_min, y_min], [x_max, y_min]) #linea inferior
    left = bresenham([x_min, y_min], [x_min, y_max]) #linea de la izquierda
    right = bresenham([x_max, y_min], [x_max, y_max]) #linea de la derecha
    lineas = [bottom, top, left, right]

    for linea in lineas:
        pintar_linea(linea, color=(0,200,100))

def pintar_linea(puntos, color=(0,0,0)):
    for punto in puntos:
        put_pixel(punto[0], punto[1], color=color)

def dibujar_cuadrado(origen, size, color=(255,0,0)):
    vertices = [ origen, (origen[0], origen[1]+size), (origen[0]+size, origen[1]+size), (origen[0]+size, origen[1]) ]
    vertices_color = []
    #print("inicio: ", origen)
    for y in range(origen[1], origen[1]+size+1):
        vertices_color += bresenham((origen[0], y), (origen[0]+size, y))
    pintar_viewport_vertices(vertices_color)
    #print("lineas: ", vertices_color)

def pintar_poligono(puntos, color=(0,0,0)):
    for i in range(0, len(puntos)-1): # range(0,4*) 4, 5
        puntos_recta = bresenham(puntos[i], puntos[i+1])
        pintar_linea(puntos_recta, color=color) # pendiente verificar 
    ultima_recta = bresenham(puntos[0], puntos[-1])
    pintar_linea(ultima_recta, color=color)
# bucle infinito para mostrar en patalla todos los elementos gráficos.

""" Puntos de la EII y la ESD """
def definir_viewport_E():
    print("Ingrese los valores de la EII y la ESD del viewport")
    x1 = int(input("Ingrese x1: "))
    y1 = int(input("Ingrese y1: "))
    x2 = int(input("Ingrese x2: "))
    y2 = int(input("Ingrese y2: "))
    
    return [(x1,y1), (x2,y2)]

def definir_viewport_TBLR():
    top = int(input("Ingrese el valor para TOP: "))
    bottom = int(input("Ingrese el valor para BOTTOM: "))
    left = int(input("Ingrese el valor para LEFT: "))
    right = int(input("Ingrese el valor para RIGHT: "))

    return [top, bottom, left, right]

def definir_viewport_puntos():
    num_vertices = int(input("Ingrese el número de vértices del polígono de recorte (viewport): "))
    print("Ingrese los valores de cada punto para el viewport (en sentido horario)")
    lista_vertices = list()
    for i in range(num_vertices):
        lista_vertices.append((int(input(f"Ingrese x{i}: ")),int(input(f"Ingrese y{i}: "))))
    return lista_vertices

def ingresar_datos_linea():
    print("Ingrese los puntos inicial y final de la línea")
    x1 = int(input("Ingrese x1: "))
    y1 = int(input("Ingrese y1: "))
    x2 = int(input("Ingrese x2: "))
    y2 = int(input("Ingrese y2: "))

    return (x1,y1),(x2,y2)
    
def ingresar_datos_poligono():
    num_vertices = int(input("Ingrese el número de vértices del polígono: "))
    vertices_poligono = []
    for i in range(num_vertices):
        print(f"vértice {i}:")
        vertices_poligono.append(tuple([int(input("ingrese el valor de x: ")), int(input("ingrese el valor de y: "))]))
    return n, vertices_poligono

def seleccionar_algoritmo_linea():
    print("Seleccione el número del algoritmo que quiere usar:")
    print("1. Cohen-Sutherland")
    print("2. Cyrus-Beck")
    alg = int(input("Algoritmo: "))
    return alg

def seleccionar_algoritmo_poligono():
    print("Seleccione el número del algoritmo que quiere usar:")
    print("1. Sutherland-Hodgman")
    print("2. Weiler-Atherton")
    alg = int(input("Algoritmo: "))
    return alg

def puntos_a_string(puntos):
    lista = ""
    for punto in puntos:
        lista += str(punto[0])
        lista += " "
        lista += str(punto[1])
        lista += " "
    return lista

def agrupar(lista, n):
    i = 0
    nlista = [] #Lista
    while(i < len(lista)):
        nlista.append(lista[i:i+n])
        i += n
    return list(nlista)

setup() #pantalla

#Clase utilizada para mostrar el robot en pantalla.
class Robot():
    def __init__(self, x, y, tam, color):
        self.x = y
        self.y = x
        self.color = color
        self.tam = tam
    
    def pintar(self):
        dibujar_cuadrado((self.x, self.y), self.tam, color=self.color) #posicion x, posicion y, ancho, alto.

    def mover(self, direccion):
        if direccion == "izquierda":
            self.x -= self.tam
        elif direccion == "derecha":
            self.x += self.tam
        elif direccion == "arriba":
            self.y -= self.tam
        elif direccion == "abajo":
            self.y += self.tam

def mostrar_juego(tipo_viewport=None): 
    while True:        
        for event in pg.event.get():
            if event.type == pg.QUIT: #para detener la ejecución al cerrar la ventana
                pg.quit()
                sys.exit()
        
        #pintar_linea(bresenham(P1,P2), (200,200,0))
        #put_pixel(0, 0, (121,0,128)) #mostrar punto de origen relativo
        #pintar_poligono([[10,10], [20,10], [30, 20], [20, 30], [10, 30],[0,20]])
        #pintar_poligono(((0,0),(100,0),(50,100)))
        #pol = [[100, 290], [100, 210], [275, 230], [150, 250], [275, 270], [100, 290]]
        #pintar_poligono(pol)
        #grid() #mostrar la cuadrícula.
        
        #robot.mover("derecha")
        robot.pintar()
        #dibujar_cuadrado((0,0), 5)
        #put_pixel(0, 0, color=(200,250,0))
        #put_pixel(0, 5, color=(0,0,250))

        #pantalla.fill((255, 255, 255))
        pg.display.update()
        pg.display.flip() #actualizar el mundo para mostrar nuevos cambios.


if __name__ == "__main__":
    x0 = 0
    y0 = 0
    
    robot = Robot(x0, y0, normal_size, (255,100,0))
    robot.pintar()
    mostrar_juego()