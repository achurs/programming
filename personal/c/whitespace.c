#include <stdio.h>
#include <string.h>
void main(){
    int l,count = 0;
    char c[100];
    printf("enter the string\n");
    gets(c);
    l=strlen(c);
    for(int i=0;i<l;i++)
    {
        if(c[i]==' ')
        {
            printf("%c",c[i]);
            count++;
        }
    }
    printf("the number of whitespace is %d",count);
}