#include <stdio.h>

void update(int *a,int *b) {
    // Complete this function    
    int total,p;
    total = *a + *b;
    p = *a - *b;
    *a = total;
    if (p < 0 )
    {
        p = - p;
    }
    *b = p;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}