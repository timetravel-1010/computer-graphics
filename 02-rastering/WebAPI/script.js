const WIDTH = 800;
const HEIGHT = 800;
const BSIZE = 40;

function init() {
  var acanvas = document.getElementById('acanvas')
  acanvas.width  = WIDTH;
  acanvas.height = HEIGHT;
  var ctx = acanvas.getContext("2d");

  for (let i = 0; i < WIDTH; i += 1) {
      for (let j = 0; j < HEIGHT; j += 1) {
          ctx.fillStyle = "gray";
          ctx.fillRect(i*BSIZE, i*BSIZE, BSIZE, BSIZE);
          ctx.strokeStyle = "gray";
          ctx.strokeRect(i*BSIZE, j*BSIZE, BSIZE, BSIZE);//for white background
      }
  }    
}