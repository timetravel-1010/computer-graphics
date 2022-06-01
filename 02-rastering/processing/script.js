const BSIZE = 20;

const ROWS = 25; /* Creo que esto es lo que ingresa el usuario */
const COLUMNS = ROWS; /* Lo de arriba */

const WIDTH = BSIZE*COLUMNS; 
const HEIGHT = BSIZE*ROWS;

/* Cuadrado azul oscuro. */
let origenX = 11;  
let origenY = 11;

/* Cuadrado azul claro */
let nuevoOrigenX = -2; /* 0 si no cambia el origen */
let nuevoOrigenY = -3; /* 0 si no cambia el origen */

let radio = 8;

let points = midPointCircleDraw(0, 0,/* En todo caso se debe dejar con centro (0,0) */
                                radio); /* Si se pide otro centro se cambia en las variables nuevoOrigen */
console.log(points)

/**
 * Función principal para utilizar processing.
 * @param {} processing 
 */
function sketch(processing){

    /**
     * setup: configuración inicial. (pantalla y tasa de fotogramas)
     */
    processing.setup = function() {
      processing.frameRate(2); // fps
		  processing.size(WIDTH, HEIGHT);
    }

    /**
     * Función que pinta todo en el lienzo.
     * @param {estado actual del mundo} world 
     */
    processing.drawCanvas = function(world) {
      
      for (let i = 0; i < ROWS; i += 1) {
        for (let j = 0; j < COLUMNS; j += 1) {
          processing.fill(130, 130, 130);
          processing.rect(j*BSIZE, i*BSIZE, BSIZE, BSIZE);
        }
      }
      drawFullCircle(points)
      processing.fill(0, 0, 100)
      processing.rect(origenX*BSIZE, origenY*BSIZE, BSIZE, BSIZE) // punto de origen (0,0)
      processing.fill(0, 204, 204)
      processing.rect((origenX + nuevoOrigenX)*BSIZE, (origenY - nuevoOrigenY)*BSIZE, BSIZE, BSIZE) // punto de origen arbitrario.
    }

    processing.onTic = function(world) {

    }

    processing.onMouseEvent = function (world, event) {
      return world;
    }

    /**
     * Función utilizada para pintar puntos.
     * @param {list_of_points} points lista de puntos a pintar.
     */
    function drawPoints(points) {
      
      processing.fill(0,0,0)
      let j = 30;
      
      for (let i = 0; i<=points.length-1; i+=1) {
        processing.rect( (points[i][0] + (origenX + nuevoOrigenX)) * BSIZE, 
                         ((origenY - nuevoOrigenY) - points[i][1]) * BSIZE, 
                         BSIZE, BSIZE)
      } 
    }

    /**
     * Función usada para obtener el reflejo de los puntos de una lista en los otros cuadrantes.
     * @param {list_of_points} points lista de puntos iniciales.
     * @returns nueva lista de puntos.
     */
    function mirror(points) {

      let points_reflected = [];

      for (let i = 0; i<points.length; i += 1) {
        points_reflected.push([points[i][0]*-1, points[i][1]])
        points_reflected.push([points[i][0], points[i][1]*-1])
        points_reflected.push([points[i][0]*-1, points[i][1]*-1])
        points_reflected.push([points[i][1], points[i][0]])
        points_reflected.push([points[i][1]*-1, points[i][0]])
        points_reflected.push([points[i][1], points[i][0]*-1])
        points_reflected.push([points[i][1]*-1, points[i][0]*-1])
      }
      return points_reflected;
    }

    /**
     * Función utilizada para pintar un círculo por completo.
     * @param {list_of_points} points lista de puntos de un octante de círculo.
     */
    function drawFullCircle(points) {
      let points_reflected = mirror(points) //se obtienen los otros puntos para completar el círculo.
      let j = 30;
      processing.fill(183,183,183);
      
      for (let i = 0; i<=points_reflected.length-1; i+=1) {
        processing.rect( (points_reflected[i][0] + (origenX + nuevoOrigenX)) * BSIZE, 
                         ((origenY - nuevoOrigenY) - points_reflected[i][1]) * BSIZE, 
                         BSIZE, BSIZE)
      } 
      drawPoints(points) //se pintan los puntos que retorna el algoritmo.
    }

    function drawCircleCentre(x_centre, y_centre, r) {
      let points = midPointCircleDraw(x_centre, y_centre,r);
      processing.fill(10, 10, 10)
      processing.rect((x_centre+origenX)*BSIZE, (origenY-y_centre)*BSIZE, BSIZE, BSIZE)
      processing.fill(0,0,0)
      let j = 30;
      for (let i = 0; i<=points.length-1; i+=1) {
        // Pendiente verificar 
        processing.rect((points[i][0]+origenX)*BSIZE, (origenY-points[i][1])*BSIZE, BSIZE, BSIZE)
        //processing.rect((points[i][1]+origenX)*BSIZE, (origenY-points[i][0])*BSIZE, BSIZE, BSIZE)
      } 
    }


    /**
     * Función utilizada para pintar un cuadrado con la diferencia de que se invierten las coordenadas
     * x y y de cada punto de la lista.
     * @param {list_of_points} points lista de puntos de la forma (y, x).
     */
    function drawLineReverse(points) {
      processing.fill(0,0,0)

      let j = 30;

      for (let i = 0; i<=points.length-1; i+=1) {
        processing.rect(points[i][1]*BSIZE, (j-points[i][0])*BSIZE, BSIZE, BSIZE)
      } 
    }

    function drawCircle(points) {
      processing.fill(0, 0, 0)
      let j = 30;
      for (let i = 0; i<=points.length-1; i+=1) {
        processing.rect(points[i][0]*BSIZE, (j-points[i][1])*BSIZE, BSIZE, BSIZE)
        processing.rect(points[i][1]*BSIZE, (j-points[i][0])*BSIZE, BSIZE, BSIZE)
      } 
    }


  // ******************** De aquí hacia abajo no debe cambiar nada. ********************

  // Esta es la función que pinta todo. Se ejecuta 60 veces por segundo. 
  // No cambie esta función. Su código debe ir en drawGame
  processing.draw = function () {
    processing.drawCanvas(processing.state);
    processing.state = processing.onTic(processing.state);
  };
  // Esta función se ejecuta cada vez que presionamos una tecla. 
  // No cambie esta función. Su código debe ir en onKeyEvent
  processing.keyPressed = function () {
    processing.state = processing.onKeyEvent(processing.state, processing.keyCode);
  }
  // Esta función se ejecuta cada vez movemos el mouse. 
  // No cambie esta función. Su código debe ir en onKeyEvent
  processing.mouseMoved = function () {
    processing.state = processing.onMouseEvent(processing.state,
      { action: "move", mouseX: processing.mouseX, mouseY: processing.mouseY });
  }

  // Estas funciones controlan los eventos del mouse. 
  // No cambie estas funciones. Su código debe ir en OnMouseEvent
  processing.mouseClicked = function () {
    processing.state = processing.onMouseEvent(processing.state,
      { action: "click", mouseX: processing.mouseX, mouseY: processing.mouseY, mouseButton: processing.mouseButton });
  }

  processing.mouseDragged = function () {
    processing.state = processing.onMouseEvent(processing.state,
      { action: "drag", mouseX: processing.mouseX, mouseY: processing.mouseY, mouseButton: processing.mouseButton });
  }

  processing.mousePressed = function () {
    processing.state = processing.onMouseEvent(processing.state,
      { action: "press", mouseX: processing.mouseX, mouseY: processing.mouseY, mouseButton: processing.mouseButton });
  }

  processing.mouseReleased = function () {
    processing.state = processing.onMouseEvent(processing.state,
      { action: "release", mouseX: processing.mouseX, mouseY: processing.mouseY, mouseButton: processing.mouseButton });
  }
  // Fin de los eventos del mouse


}

const canvas = document.getElementById("canvas");
const instance = new Processing(canvas, sketch);