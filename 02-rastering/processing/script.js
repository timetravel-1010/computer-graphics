const WIDTH = 800;
const HEIGHT = 800;
const BSIZE = 40;


function sketch(processing){

    processing.setup = function(){
      processing.frameRate(2); // fps
		  processing.size(WIDTH, HEIGHT);
    }
    processing.drawCanvas = function(world){
      
      for (let i = 0; i < 20; i += 1) {
        for (let j = 0; j < 20; j += 1) {
          processing.fill(84, 84, 69);
          processing.rect(j*BSIZE, i*BSIZE, BSIZE, BSIZE)
          
          processing.fill(255, 255, 204);
          processing.rect(i*BSIZE, i*BSIZE, BSIZE, BSIZE) // Draw diagonal line
        }
      }
    }
    processing.onTic = function(world) {
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