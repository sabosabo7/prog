#include <stdio.h>

int main()
{
    double x, sum;
    sum = 0;
    int n = 0;
    for (x = 0.1; x <= 1; x += 0.1)
    {
        n += 1;
        sum += x;
        // printf("%f\n", x);
    }
    printf("%f %f %i\n", sum, x, n);
    return 0;
}