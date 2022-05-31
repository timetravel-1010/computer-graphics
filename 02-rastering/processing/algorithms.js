function drawLineBasic(x1, y1, x2, y2){
    let points = []
    dx = Math.abs(x2-x1);
    dy = Math.abs(y2-y1);
    m = dy/dx;
    if (m >= 0 && m <= 1){
        //xi, yi;
        i = x1;c
        yi=y1;
        while(i <= x2){
            xi = i;
            points.push([xi, Math.round(yi)]);
            yi = yi+m;
            i=i+1;
        }
        return points
    }
}

function drawLineDDA(x1, y1, x2, y2) {
  let points = []
  dx=Math.abs(x2-x1);
  dy=Math.abs(y2-y1);
  let step = 0;

  if(dx>=dy)
      step=dx;
  else
      step=dy;

  dx=dx/step;
  dy=dy/step;

  xi=x1;
  yi=y1;
  i=1;
  
  while(i<=step+1){
      xi=xi+dx;
      yi=yi+dy;
      i=i+1;
      points.push([Math.round(xi), Math.round(yi)])
  }
  return points
}

/**
 * Función que implementa el algoritmo de Bresenham para dibujar líneas.
 * No funciona para pendientes < 1 (<- Cuidado, el valor se aproxima).
 * @param {x inicial} x1 
 * @param {y inicial} y1 
 * @param {x final} x2 
 * @param {y final} y2 
 */
function drawLineBres(x1, y1, x2, y2){
    let points = []
    let m_new = 2 * (y2 - y1); 
    let slope_error_new = m_new - (x2 - x1);

    for (let x = x1, y = y1; x <= x2; x += 1) {
 
        points.push(x,y )
    
       // Add slope to increment angle formed
       slope_error_new += m_new;
    
       // Slope error reached limit, time to
       // increment y and update slope error.
       if (slope_error_new >= 0) {
          y++;
          slope_error_new  -= 2 * (x2 - x1);
       }
    }
 }

 /**
 * Función que implementa el algoritmo de Bresenham para dibujar líneas.
 * Funciona para cualquier pendiente.
 * @param {x inicial} x1 
 * @param {y inicial} y1 
 * @param {x final} x2 
 * @param {y final} y2 
 */
 function bresenham(x1 , y1 , x2,y2)
 {
     var m_new = 2 * (y2 - y1);
     var slope_error_new = m_new - (x2 - x1);
  
     for (x = x1, y = y1; x <= x2; x++)
     {
         console.log("(" +x + "," + y + ")\n");

         // Add slope to increment angle formed
         slope_error_new += m_new;

         // Slope error reached limit, time to
         // increment y and update slope error.
         if (slope_error_new >= 0)
         {
             y++;
             slope_error_new -= 2 * (x2 - x1);
         }
     }
 } 


//export  {drawLineBasic}

function midPointCircleDraw(x_centre, y_centre, r) {
    let x = r, y = 0
    let points = []
    // Printing the initial point on the axes
    // after translation
    points.push([x + x_centre, y + y_centre])
     

     
    // Initialising the value of P
    let P = 1 - r

    while (x > y) {
        y += 1
        // Mid-point is inside or on the perimeter
        if (P <= 0)
            P = P + 2*y + 1;
        // Mid-point is outside the perimeter
        else {
            x -= 1;
            P = P + 2*y - 2*x + 1;
        }
         
        // All the perimeter points have already been printed
        if (x < y)
            break;
         
        // Printing the generated point and its reflection
        // in the other octants after translation
        points.push([x + x_centre, y + y_centre]);
    }
    return points
}
//console.log(midPointCircleDraw(0,0,10))
//console.log(drawLineBasic(18,9,26,12))
console.log(bresenham(9,18,14,22))

