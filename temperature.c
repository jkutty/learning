#include <stdio.h>

#define UPPER 450 /* upper limit of table*/
#define LOWER 0   /* lower limit of table*/
#define STEP 50   /* step size*/

/* print Farenheit to Celsius table */
int main()
{
    int fahr;

    printf("  F \t C\n");
    for (fahr = LOWER; fahr <= UPPER; fahr = fahr + STEP)
        printf("%3d |%6.1f\n", fahr, (5.0/9.0)*(fahr-32));
}