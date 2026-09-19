#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    
    char ch;
    char l[100];
    char full[101];
    
    scanf("%c",&ch);     
    scanf("%s",l); 
    scanf(" %[^\n]",full);
    
    printf("%c\n",ch);   
    printf("%s\n",l);  
    printf("%s",full); 
    
    return 0;

}
