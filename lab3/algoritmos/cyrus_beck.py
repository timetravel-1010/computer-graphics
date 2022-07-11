import numpy as np

#vertices = [[10,10], [20,10], [20,20], [10,20]]
#[[200, 50], [250, 100], [200, 150], [100, 150], [50, 100], [100, 50]]
# parece ser que los vertices van en sentido antihorario
n = 4

def dot(x1, y1, x2, y2):
    return x1 * x2 + y1 * y2

def CyrusBeckClip(P1, P2, EII, ESD):
    x1, y1 = P1
    x2, y2 = P2
    x_min, y_min = EII
    x_max, y_max = ESD
    vertices = [[x_min, y_min], [x_max, y_min], [x_max, y_max], [x_min, y_max]]
    normal = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    for i in range(0, n):
        normal[i][1] = vertices[(i + 1) % n][0] - vertices[i][0]
        normal[i][0] = vertices[i][1] - vertices[(i + 1) % n][1]

    dx = x2 - x1
    dy = y2 - y1

    dp1e = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    for i in range(0, n):
        dp1e[i][0] = vertices[i][0] - x1
        dp1e[i][1] = vertices[i][1] - y1

    numerator = [0, 0, 0, 0, 0, 0]
    denominator = [0, 0, 0, 0, 0, 0]

    for i in range(0, n):
        numerator[i] = dot(normal[i][0], normal[i][1], dp1e[i][0], dp1e[i][1])
        denominator[i] = dot(normal[i][0], normal[i][1], dx, dy)

    t = [0, 0, 0, 0, 0, 0]
    tE = np.array([0])
    tL = np.array([1])

    for i in range(0, n):
        t[i] = float(numerator[i]) / float(denominator[i])
        if denominator[i] > 0:
            tE = np.append(tE, t[i])
        else:
            tL = np.append(tL, t[i])

    temp0 = np.amax(tE)
    temp1 = np.amin(tL)

    if temp0 > temp1:
        return

    New_X1 = float(x1) + float(dx) * float(temp0)
    New_Y1 = float(y1) + float(dy) * float(temp0)
    New_X2 = float(x1) + float(dx) * float(temp1)
    New_Y2 = float(y1) + float(dy) * float(temp1)
    puntos =  [[int(New_X1), int(New_Y1)], [int(New_X2), int(New_Y2)]]
    #print("nuevos puntos: ", puntos)
    return puntos
    

if __name__ == '__main__':
    """ x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    x2 = int(input("x2: "))
    y2 = int(input("y2: ")) """
    x1 = 1
    y1 = 1
    x2 = 11
    y2 = 15
    vertices = [[10,10], [20,10], [20,20], [10,20]]
    resultado = CyrusBeckClip([x1,y1], [x2,y2], [10,10], [20,20])
    print("nuevos puntos: ", resultado)