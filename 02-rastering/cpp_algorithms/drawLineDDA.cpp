#include<iostream>
#include <math.h>

using namespace std;
 
void drawLineDDA(int x1, int y1, int x2, int y2){
    float dx=abs(x2-x1);
    float dy=abs(y2-y1);
    float step;

    if(dx>=dy)
        step=dx;
    else
        step=dy;

    dx=dx/step;
    dy=dy/step;
    
    float xi,yi;

    xi=x1;
    yi=y1;
    int i=1;
    while(i<=step+1){
        cout << "i: "<< i <<" (" << roundf(xi) << ", " << roundf(yi) << ") step: "<< step <<"\n";
        xi=xi+dx;
        yi=yi+dy;
        i=i+1;
    }
}
 
// Driver code
int main(){
    drawLineDDA(-1, 1, 3, 3);
    return 0;
}
