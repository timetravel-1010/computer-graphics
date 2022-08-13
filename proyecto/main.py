from algoritmos.preferencia_amplitud import preferencia_amplitud
import interface

if __name__ == '__main__':
    #origen de coordenadas, cambiar en caso de necesitar
    x0 = 0
    y0 = 0
    mundo = interface.input("mundo") #x0, y0 posición inicial del robot.
    while True:
        x0 = int(input("Ingrese la coordenada x (entre 0 y 9): "))
        y0 = int(input("Ingrese la coordenada y (entre 0 y 9): "))
        valor = mundo[x0][y0]
        if (valor == 0 or valor == 6):
            mundo[x0][y0] = 2
            break
        else: 
            print("Por favor ingrese una coordenada válida.")
    resultado = preferencia_amplitud(mundo, x0, y0)
    interface.mostrar_juego(resultado, (x0, y0))