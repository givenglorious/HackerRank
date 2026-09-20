#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
  //Write your code here.
  int a,o,x;
  int max_a= 0,max_o = 0,max_x = 0;
  for (int i = 1; i <= n;i++)
  {
    for(int j = i + 1;j <= n;j++)
    {
        a = i & j;
        x = i ^ j;
        o = i | j;
        if(a < k && a > max_a)
        {
            max_a = a;
        }

        
        if (x < k && x > max_x)
        {
            max_x = x;
        }
        
        if (o < k && o > max_o)
        {
            max_o = o;
        }
    }
    
  }
    printf("%d\n",max_a);
    printf("%d\n",max_x);
    printf("%d\n",max_o);
  
  
  
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
