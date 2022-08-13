import pygame as pg
import os, sys
import numpy as np

from algoritmos.rastering.bresenham import bresenham

n = 480 #matriz nxn, 480 -> 1:1 pixel
ancho = 640 #ancho de la pantalla
alto = ancho
size = ancho // n #tamaño del lado de cada *pixel*

normal_size = ancho // 10 #10 -> número de columnas y filas
ticks = 5 #velocidad del reloj, mayor número -> mayor velocidad
colores = { 0:(255,255,255), #casilla libre
            1:(150,75,0), #muros
            2:(0,123,123), #punto de inicio
            3:(0, 255, 0), #primer nave
            4:(204,204,255), #segunda nave
            5:(255,255,0), #un ítem
            6:(255,0,0), #aceite
        }

""" 
configuración inicial de la pantalla 
"""
def setup():
    global pantalla 
    pg.init()
    pantalla = pg.display.set_mode((ancho, alto))
    pg.display.set_caption('Smart RobotUI')
    pantalla.fill((255,255,255)) 

""" 
función usada para leer el archivo txt del mundo inicial, reciba
el nombre del archivo sin la extensión .txt
"""
def input(nombre_lectura):
    with open(f"mundos/{nombre_lectura}.txt", "r") as f:
        content = f.read().split('\n')
        mundo = []
        for i in range(10):
            fila = list(map(lambda x: int(x), content[i].split(" ")))
            mundo.append(fila)
        return np.array(mundo)

""" 
función usada para crear la cuadrícula 
"""
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
Recibe una coordenada x y y para el pixel y opcionalmente su color
"""
def put_pixel(x, y, color=(0,0,0)):
    global size
    pg.draw.rect(pantalla, color, (x*size, y*size, size, size))


""" 
función para el dibujo de una línea dados sus puntos y opcionalmente su color.
"""
def pintar_linea(puntos, color=(0,0,0)):
    for punto in puntos:
        put_pixel(punto[0], punto[1], color=color)

def dibujar_cuadrado(origen, size, color=(255,0,0)):
    vertices = [ origen, (origen[0], origen[1]+size), (origen[0]+size, origen[1]+size), (origen[0]+size, origen[1]) ]
    vertices_color = []
    for y in range(origen[1], origen[1]+size+1):
        vertices_color += bresenham((origen[0], y), (origen[0]+size, y))
    pintar_poligono(vertices_color, color=color)

def pintar_poligono(puntos, color=(0,0,0)):
    for i in range(0, len(puntos)-1): # range(0,4*) 4, 5
        puntos_recta = bresenham(puntos[i], puntos[i+1])
        pintar_linea(puntos_recta, color=color) # pendiente verificar 
    ultima_recta = bresenham(puntos[0], puntos[-1])
    pintar_linea(ultima_recta, color=color)


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

def pintar_mundo(mundo):
        x = 0
        y = 0
        tam = normal_size #tamaño de cada cuadro.

        for fila in mundo: #recorre las filas.
            for valor in fila: #recorre cada elemento de la fila.
                dibujar_cuadrado((x, y), tam, color=colores.get(valor)) #posicion x, posicion y, ancho, alto.           
                x += tam
            x = 0
            y += tam

def mostrar_juego(resultado, inicio_robot): 
    setup() #pantalla
    
    robot = Robot(inicio_robot[0]*normal_size, inicio_robot[0]*normal_size, normal_size, (0,230,230))
    resultado = resultado[0]
    clock = pg.time.Clock() #reloj para manipular la velocidad de la ejecución.
    i = len(resultado)-1

    while True:        
        clock.tick(ticks) 

        for event in pg.event.get():
            if event.type == pg.QUIT: #para detener la ejecución al cerrar la ventana
                pg.quit()
                sys.exit()
        
        if (i >= 0):
            try:
                pintar_mundo(resultado[i][1]) #pinta el mundo correspondiente al nodo actual.
                
                robot.mover(resultado[i][0]) #se obtiene el operador para mover el robot. 
                print("movimiento: ", resultado[i][0])
                print("combustible_actual:", resultado[i][2])
                print("costo: ", resultado[i][3])
                robot.pintar()
            except ValueError:
                print("No se encontró la solución.")
        i -= 1

        grid() #mostrar la cuadrícula
        pg.display.flip() #actualizar el mundo para mostrar nuevos cambios.