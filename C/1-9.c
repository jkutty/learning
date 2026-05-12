#include <stdio.h>

int main()
{
    int c;
    int prev_was_space;
    c = 0;
    prev_was_space = 0;
    while ((c = getchar()) != EOF)
        if( c != ' ' ){
            putchar( c );
            prev_was_space = 0;
        }
        else{
            if( prev_was_space == 0 ){
                printf( " " );
                prev_was_space = 1;
            }
        }
}