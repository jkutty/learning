#include <stdio.h>

/* copy input to output */
/* verify expression */

int main()
{
    int c;

    while (c = (getchar() != EOF))
        printf("%d\n", c);
}