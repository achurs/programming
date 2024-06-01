#include<stdio.h>
void main()
{
    int arr[100],arr1[100],arr2[100],i,c1=0,c2=0,n;
    printf("Enter the number of  elements to be inputted\n");
    scanf("%d",&n);
    printf("Enter the elements\n");
    
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    for(i=0;i<n;i++)
    {
        if(arr[i]%2==0)
        {
            arr1[c1]=arr[i];
            c1++;
        }
        else
        {
            arr2[c2]=arr[i];
            c2++;
        }
    }
    printf("\nThe even numbers are\n");
    for(i=0;i<c1;i++)
    {
        printf("%d ",arr1[i]);
    }
    printf("\nThe odd numbers are\n");
    for(i=0;i<c2;i++)
    {
        printf("%d ",arr2[i]);
    }
}