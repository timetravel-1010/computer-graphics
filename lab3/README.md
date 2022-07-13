## Requisitos

Para la ejecución del programa es necesario instalar las dependencias, puede hacerlo de la siguiente forma:

`pip install -r requirements.txt`

## Ejecución

La ejecución del programa se realiza desde una terminal así:

`python menu.py`

## Uso

Puede modificar el origen del plano cartesiano que se usa para graficar cambiando los valores de x0 y y0 de las líneas 23 y 24 respectivamente en el archivo `interfaz.py`. Cabe resaltar que estos valores indican el origen con respecto al sistema de referencia de la ventana (aumenta en x a la derecha y en y hacia abajo).

Modificando la variable `n` de la líena 17 del archivo `interfaz.py` se puede obtener una matriz nxn a conveniencia.

Adicionalmente se puede modificar el tamaño de la pantalla cambiando el valor de la variable `ancho` en la línea 18 del archivo `interfaz.py`.

## Importante

Para el correcto funcionamiento de algunos algoritmos de deben ingresar los puntos del polígono y/o viewport en sentido horario.

## Ejemplos

A continuación se muestran algunos ejemplos para evidenciar el correcto uso del programa.

Puede encontrar estos y otros ejemplos en el archivo `ejemplos.txt`.

### Modificación de n y x0

En caso de ser requerido, se puede modificar el valor del tamaño de una casilla (n) y la coordenada x0 que sirve para el origen (0,0) del marco de referencia cartesiano usado para la graficación.

Lo anterior se realiza en las líneas 17 para n y 23 para x0, del archivo `interfaz.py` como se muestra en la siguiente imagen.

![modificar n y x0](/img/modificar-n-y-x0.png)

Adicionalmente, puede modificar el valor de y0 (línea 24) para cambiar la coordenada y del origen (0,0) en la pantalla.


### Ejemplo 1. Algoritmo Cohen-Sutherland

![ejemplo 1 Cohen-Sutherland](/img/ejemplo1-Cohen-Sutherland.png)

### Ejemplo 2. Algoritmo Cohen-Sutherland

![ejemplo 2 Cohen-Sutherland](/img/ejemplo2-Cohen-Sutherland.png)

### Ejemplo Algoritmo Cyrus-Beck

![ejemplo Cyrus-Beck](/img/ejemplo1-Cyrus-Beck.png)

### Ejemplo Algoritmo Sutherland-Hodgman

![ejemplo Sutherland-Hodgman](/img/ejemplo1-Sutherland-Hodgman.png)

### Ejemplo Algoritmo Weiler-Atherton

![ejemplo Weiler-Atheron](/img/ejemplo1-Weiler-Atherton.png)