//let radio = 8;
//let points = midPointCircleDraw(0, 0,/* En todo caso se debe dejar con centro (0,0) */
//                                radio); /* Si se pide otro centro se cambia en las variables nuevoOrigen */

//let points = midPointCircleDraw(0,0,8)
//var COLUMNS = 30;
//var ROWS = 30;
var ROWS = prompt("Filas: ");
var COLUMNS = prompt("Columnas: ");
var points = [0, 0, 0, 0]

/* Cuadrado azul oscuro. */
let origenX = 2;  
let origenY = ROWS-2;

const BSIZE = 20;

var WIDTH = BSIZE*COLUMNS; 
var HEIGHT = BSIZE*ROWS;

/* Cuadrado azul claro */
let nuevoOrigenX = 0; /* 0 si no cambia el origen */
let nuevoOrigenY = 0; /* 0 si no cambia el origen */

function mostrarDibujo() {
  var x1 = parseInt(document.getElementById("x1").value);
  var x2 = parseInt(document.getElementById("x2").value);
  var y1 = parseInt(document.getElementById("y1").value);
  var y2 = parseInt(document.getElementById("y2").value);
  var radio = parseInt(document.getElementById("radio").value);

  origenX = parseInt(document.getElementById("origenX").value);
  origenY = parseInt(document.getElementById("origenY").value);

  answer = document.getElementById("algorithm");
  var selected = answer.options[answer.selectedIndex].text;

  if (selected == "L. Basic") {
    if ((y2-y1)/(x2-x1) < 1)
      points = [0, drawLineBasic(x1, y1, x2, y2)]
    else 
      points = [1, drawLineBasic(y1, x1, y2, x2)]
  }
  else if (selected == "L. DDA") {
    points = [0, drawLineDDA(x1, y1, x2, y2)]
  }
  else if (selected == "L. Bresenham") {
    if ((y2-y1)/(x2-x1) < 1)
      points = [0, drawLineBresenham(x1, y1, x2, y2)]
    else 
      points = [1, drawLineBresenham(y1, x1, y2, x2)]
  }
  else if (selected == "C. Midpoint") { 
    points = [2, midPointCircleDraw(0, 0, radio)]
    nuevoOrigenX = x1;
    nuevoOrigenY = y1;
  }
  console.log(points)
}





/**
 * Función principal para utilizar processing.
 * @param {} processing 
 */
function sketch(processing){


      /* ******************** Clases ******************** */


  class Drawer {
    constructor() {

    }

  /**
   * Función utilizada para pintar puntos.
   * @param {list_of_points} points lista de puntos a pintar.
   */
  drawPoints(points) {
      processing.fill(0,0,0)
      let j = 30;
      
      for (let i = 0; i <= (points.length - 1); i+=1) {
          processing.rect( (points[i][0] + (origenX + nuevoOrigenX)) * BSIZE, 
                          ((origenY - nuevoOrigenY) - points[i][1]) * BSIZE, 
                          BSIZE, BSIZE)
      } 
  }

  /**
   * Función utilizada para pintar un cuadrado con la diferencia de que se invierten las coordenadas
   * x y y de cada punto de la lista.
   * @param {list_of_points} points lista de puntos de la forma (y, x).
   */
  drawLineReverse(points) {
      processing.fill(0,0,0)

      let j = 30;

      for (let i = 0; i <= (points.length - 1); i+=1) {
          processing.rect( (points[i][1] + (origenX + nuevoOrigenX)) * BSIZE, 
                          ((origenY - nuevoOrigenY) - points[i][0]) * BSIZE, 
                          BSIZE, BSIZE)
      } 
  }

  /**
   * Función utilizada para pintar un círculo por completo.
   * @param {list_of_points} points lista de puntos de un octante de círculo.
   */
  drawFullCircle(points) {
    
      let points_reflected = this.mirror(points) //se obtienen los otros puntos para completar el círculo.
      
      console.log("reflected points: ", points_reflected)
      let j = 30;
      processing.fill(183,183,183);
      
      for (let i = 0; i<=points_reflected.length-1; i+=1) {
      processing.rect( (points_reflected[i][0] + (origenX + nuevoOrigenX)) * BSIZE, 
                      ((origenY - nuevoOrigenY) - points_reflected[i][1]) * BSIZE, 
                      BSIZE, BSIZE)
      } 
      this.drawPoints(points) //se pintan los puntos que retorna el algoritmo.
  }

  /**
   * Función usada para obtener el reflejo de los puntos de una lista en los otros cuadrantes.
   * @param {list_of_points} points lista de puntos iniciales.
   * @returns nueva lista de puntos.
   */
  mirror(points) {
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
}

/* ******************** Fin Clases ******************** */

    console.log("datos: ")
    console.log()
    const drawer = new Drawer(origenX, origenY, nuevoOrigenX, nuevoOrigenY);

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

        processing.fill(0, 0, 100)
        processing.rect(origenX*BSIZE, origenY*BSIZE, BSIZE, BSIZE) // punto de origen (0,0)
        processing.fill(0, 204, 204)
        processing.rect((origenX + nuevoOrigenX)*BSIZE, (origenY - nuevoOrigenY)*BSIZE, BSIZE, BSIZE) // punto de origen arbitrario.
      }

              /**
     * setup: configuración inicial. (pantalla y tasa de fotogramas)
     */
    processing.setup = function() {
      processing.frameRate(2); // fps
      processing.size(WIDTH, HEIGHT);
    }


    processing.onTic = function(world) {
      if (points[0] == 0) 
        drawer.drawPoints(points[1])
      else if (points[0] == 1) 
        drawer.drawLineReverse(points[1])
      else
        drawer.drawFullCircle(points[1])
    }

    processing.onMouseEvent = function (world, event) {
        return world;
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