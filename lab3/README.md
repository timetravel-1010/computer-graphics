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