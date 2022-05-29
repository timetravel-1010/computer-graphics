#include<iostream>
using namespace std;
 
void drawLineBres(int x1, int y1, int x2, int y2){
   int m_new = 2 * (y2 - y1);
   int slope_error_new = m_new - (x2 - x1);
   for (int x = x1, y = y1; x <= x2; x++){

      cout << x << " (" << x << "," << y << ") slope: "<< m_new <<"\n";
   
      // Add slope to increment angle formed
      slope_error_new += m_new;
   
      // Slope error reached limit, time to
      // increment y and update slope error.
      if (slope_error_new >= 0)
      {
         y++;
         slope_error_new  -= 2 * (x2 - x1);
      }
   }
    
}
 
// Driver code
int main()
{
    // To draw a circle of radius 3 centered at (0, 0)
    drawLineBres(9, 18, 14, 22);
    return 0;
}