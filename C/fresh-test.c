#include <stdio.h>

int c = 0;
int s = 0;

int main(void)
{
        while(( c = getchar()) != EOF)
                if( c != ' '){
                        putchar(c);
                        s = 0;
                }
                else{
                        if( s != 1){
                        printf( " " );
                        s = 1;
                        };
                }
}