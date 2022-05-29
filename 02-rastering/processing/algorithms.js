
function midPointCircleDraw(x_centre, y_centre, r)
{
    const points = []
    let x = r, y = 0;
    // Printing the initial point on the axes
    // after translation
    points.concat([x+x_centre, y+y_centre])
     
    // When radius is zero only a single
    // point will be printed
    if (r > 0)
    {
        cout << "(" << x + x_centre << ", " << -y + y_centre << ") ";
        cout << "(" << y + x_centre << ", " << x + y_centre << ") ";
        cout << "(" << -y + x_centre << ", " << x + y_centre << ")\n";
    }
     
    // Initialising the value of P
    let P = 1 - r;
    cout << "P0= " << P <<endl;
    while (x > y)
    {
        y++;
        cout << "P" << y << "=" << P <<endl;
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
        cout << "(" << x + x_centre << ", " << y + y_centre << ") ";
         
        // If the generated point is on the line x = y then
        // the perimeter points have already been printed
        if (x != y){
            cout << "(" << y + x_centre << ", " << x + y_centre << ") \n";
        }
    }
}

midPointCircleDraw(2,2,10)