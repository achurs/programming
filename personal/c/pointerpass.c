#include <stdio.h>
void fun(int p){
    p = 20;
}
void main(){
    int a;
    a = 10;
    fun(a);
    printf("%d\n", a);
}
