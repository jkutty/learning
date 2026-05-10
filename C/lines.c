#include <stdio.h>

/* count lines in input */
int main(void)
{
    int c, b, t, nl;
    b = t = nl = 0;
    while ((c = getchar()) != EOF)
        if (c == '\n')
            ++nl;
        else if (c == '\t')
            ++t;
        else if (c == ' ')
            ++b;
    printf("%d %d %d\n", nl, t, b);
}