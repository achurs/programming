#include <stdio.h>
void main()
{
    printf("enter the total number of elements in the array\n");
    int n;
    scanf("%d",&n);
    int arr[n];
    printf("enter the elements of the array\n");
    for(int i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    printf("enter the element to be searched\n");
    int x;
    scanf("%d",&x);
    int flag=0;
    for(int i=0;i<n;i++)
    {
        if(arr[i]==x)
        {
            flag=1;
            break;
        }
    }
    if(flag==1)
    {
        printf("element found");
    }
    else
    {
        printf("element not found");
    }
}
