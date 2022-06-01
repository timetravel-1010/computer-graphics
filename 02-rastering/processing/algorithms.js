/**
 * Función que implementa el algoritmo básico incremental para dibujar líneas.
 * @param {integer} x1 coordenada x inicial.
 * @param {integer} y1 coordenada y inicial.
 * @param {integer} x2 coordenada x final
 * @param {integer} y2 coordenada y final.
 * @returns lista de puntos.
 */
function drawLineBasic(x1, y1, x2, y2){
   
    let dx = Math.abs(x2-x1);
    let dy = Math.abs(y2-y1);
    let m = dy/dx;
    let points = []

    if (m >= 0 && m <= 1) {
        //xi, yi;
        i = x1;
        yi = y1;
        while(i <= x2){
            xi = i;
            points.push([xi, Math.round(yi)]);
            yi = yi+m;
            i=i+1;
        }
        return points
    } else {
        return drawLineBasic(y1, x1, y2, x2);
    }
}

/**
 * Función que implementa el algoritmo de Bresenham para dibujar líneas.
 * @param {integer} x1 coordenada x inicial.
 * @param {integer} y1 coordenada y inicial.
 * @param {integer} x2 coordenada x final
 * @param {integer} y2 coordenada y final.
 * @returns lista de puntos
 */
function drawLineDDA(x1, y1, x2, y2) {
    let points = []
    let step = 0;

    dx=Math.abs(x2-x1);
    dy=Math.abs(y2-y1);

    if(dx>=dy)
        step=dx;
    else
        step=dy;

    dx = dx/step;
    dy = dy/step;

    xi = x1;
    yi = y1;
    i = 1;
  
    while (i<=step+1) {
        points.push([Math.round(xi), Math.round(yi)])
        xi = xi+dx;
        yi = yi+dy;
        i = i+1;
    }
    return points
}

/**
 * Función que implementa el algoritmo de Bresenham para dibujo de círculos.
 * @param {integer} x1 coordenada x inicial.
 * @param {integer} y1 coordenada y inicial.
 * @param {integer} x2 coordenada x final.
 * @param {integer} y2 coordenada y final.
 * @param {integer} dx 
 * @param {integer} dy 
 * @param {float} decide 
 * @returns lista de puntos.
 */
 function plotPixel(x1, y1, x2, y2, dx, dy, decide) {

    let pk = 2 * dy - dx;
    let points = []

    for (let i = 0; i <= dx; i++) {
        points.push([x1, y1]);

        x1 = x1 < x2 ? x1 += 1 : x1 -= 1;
        if (pk < 0) {
            if (decide == 0) 
                pk = pk + 2 * dy;
            else 
                pk = pk + 2 * dy;
        }
        else {
            y1 = y1 < y2 ? y1 += 1 : y1 -= 1;
            pk = pk + 2 * dy - 2 * dx;
        }
    }
    return points;
}
 
/**
 * Función auxiliar para implementar el algoritmo de Bresenham para dibujo de círculos.
 * @param {integer} x1 coordenada x inicial.
 * @param {integer} y1 coordenada y inicial.
 * @param {integer} x2 coordenada x final.
 * @param {integer} y2 coordenada y final.
 * @returns lista de puntos.
 */
function drawLineBresenham(x1, y1, x2, y2) {
    let points = []

    let dx = Math.abs(x2 - x1);
    let dy = Math.abs(y2 - y1);

    if (dx > dy) 
        points = plotPixel(x1, y1, x2, y2, dx, dy, 0);
    else 
        points = plotPixel(y1, x1, y2, x2, dy, dx, 1);

    return points
}

/**
 * Función que implementa el algoritmo del punto medio para dibujar círculos.
 * @param {integer} x_centre coordenada x del centro.
 * @param {integer} y_centre coordenada y del centro.
 * @param {integer} r radio del círculo.
 * @returns lista de puntos.
 */
function midPointCircleDraw(x_centre, y_centre, r) {
    let x = r, y = 0
    let points = []
    // Printing the initial point on the axes
    // after translation
    points.push([x + x_centre, y + y_centre])
    // Initialising the value of P
    let P = 1 - r;

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