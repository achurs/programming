#include <stdio.h>
#include <string.h>

int main()
{
    char str[100];
    int i, j, flag = 0;
    printf("Enter the string: ");
    gets(str);
    for (i = 0, j = strlen(str) - 1; i < j; i++, j--)
    {
        if (str[i] != str[j])
        {
            flag = 1;
            break;
        }
    }
    if (flag == 0)
        printf("The string is a palindrome");
    else
        printf("The string is not a palindrome");
    return 0;
}