from algoritmos.preferencia_amplitud import preferencia_amplitud
from interface import mostrar_juego, input, Robot

if __name__ == '__main__':
    mundo = input("mundo")
    print("mundo: ", mundo)
    x0 = 2 #x inicial del robot
    y0 = 2 #y inicial del robot
    resultado = preferencia_amplitud(mundo, x0, y0)
    mostrar_juego(resultado, (x0, y0))