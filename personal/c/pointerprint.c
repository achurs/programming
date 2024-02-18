#include <stdio.h>
int main(){
    printf("Input a number:");
    int a;
    a = 10;
    int *p = &a;
    printf("%p\n", p);
    printf("%d\n", *p);
    return 0;
}