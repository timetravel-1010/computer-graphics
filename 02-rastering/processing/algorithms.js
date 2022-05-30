function drawLineBasic(x1, y1, x2, y2){
    let points = []
    dx = Math.abs(x2-x1);
    dy = Math.abs(y2-y1);
    m = dy/dx;
    if (m >= 0 && m <= 1){
        //xi, yi;
        i = x1;
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

//export  {drawLineBasic}
/* 
function midPointCircleDraw(x_centre, y_centre, r)
{
    const points = []
    let x = r, y = 0;
    // Printing the initial point on the axes
    // after translation
    points.push([x+x_centre, y+y_centre])
    
    // When radius is zero only a single
    // point will be printed
    if (r > 0)
    {
          "("  x + x_centre  ", "  -y + y_centre  ") "
          "("  y + x_centre  ", "  x + y_centre  ") ";
          "("  -y + x_centre  ", "  x + y_centre  ")\n"; 
    }
     
    // Initializing the value of P
    let P = 1 - r;
      "P0= "  P endl;
    while (x > y)
    {
        y++;
          "P"  y  "="  P endl;
        // Mid-point is inside or on the perimeter
        if (P <= 0)
            P = P + 2*y + 1;
        // Mid-point is outside the perimeter
        else
        {
            x--;
            P = P + 2*y - 2*x + 1;
        }
         
        // All the perimeter points have already been printed
        if (x < y)
            break;
         
        // Printing the generated point and its reflection
        // in the other octants after translation
          "("  x + x_centre  ", "  y + y_centre  ") ";
         
        // If the generated point is on the line x = y then
        // the perimeter points have already been printed
        if (x != y){
              "("  y + x_centre  ", "  x + y_centre  ") \n";
        }
    }
} */

//console.log(drawLineBasic(18,9,26,12))

