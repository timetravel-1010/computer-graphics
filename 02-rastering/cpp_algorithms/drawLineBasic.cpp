#include <math.h>       /* round, floor, ceil, trunc */

#include <iostream>
using namespace std;
 
void drawLineBasic(int x1, int y1, int x2, int y2);
 
// Driver code
int main()
{
    // To draw a circle of radius 3 centered at (0, 0)
    drawLineBasic(18, 9, 26, 12);
    return 0;
}


void drawLineBasic(int x1, int y1, int x2, int y2) 
{
    float dx=abs(x2-x1);
    float dy=abs(y2-y1);
    float m = dy/dx;

    if (m >= 0 && m <= 1) 
    {
        float xi, yi;
        int i = x1;
        yi = y1;

        while (i <= x2) 
        {
            xi = i;
            cout << "(" << xi << ", " << roundf(yi) << ") \n";
            yi += m;
            i++1;
        }
    }
}
