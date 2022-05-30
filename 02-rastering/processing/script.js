//import drawLineBasic from "./algorithms";

const WIDTH = 1300;
const HEIGHT = WIDTH;
const BSIZE = 40;
const ROWS = 30;
const CELDA = WIDTH/ROWS;

//let points = drawLineBasic(18,9,26,12)
let points = drawLineDDA(-1,1,3,3)
//nuevos_puntos = points.reverse()
console.log(points) 

function sketch(processing){

    processing.setup = function(){
      processing.frameRate(2); // fps
		  processing.size(WIDTH, HEIGHT);
    }
    processing.drawCanvas = function(world){
      
      for (let i = 0; i < CELDA; i += 1) {
        for (let j = 0; j < CELDA; j += 1) {
          processing.fill(84, 84, 69);
          processing.rect(j*BSIZE, i*BSIZE, BSIZE, BSIZE)
          
          processing.fill(255, 255, 204);
          processing.rect(i*BSIZE, i*BSIZE, BSIZE, BSIZE) // Draw diagonal line
        }
      }
      drawLine(points)
    }
    processing.onTic = function(world) {

    }

    processing.onMouseEvent = function (world, event) {
        return world;
    }

    function drawLine(points) {
      processing.fill(0,0,0)
      //processing.rect(0*BSIZE, 29*BSIZE, BSIZE, BSIZE)
      let j = 30;
      for (let i = 0; i<=points.length-1; i+=1) {
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