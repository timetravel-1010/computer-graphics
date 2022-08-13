from algoritmos.preferencia_amplitud import preferencia_amplitud
from interface import mostrar_juego, input, Robot

if __name__ == '__main__':
    mundo, x0, y0 = input("mundo") #x0, y0 posición inicial del robot.
    
    resultado = preferencia_amplitud(mundo, x0, y0)
    mostrar_juego(resultado, (x0, y0))