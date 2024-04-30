#include<stdio.h>

int main()
{
    int arr[3];
    int i;

    for(i = 0; i < 3; i++)
    {
        printf("Dame el elemento [%d]: ", i);
        scanf("%d", &arr[i]);
    }

    printf("los elementos del arreglo son: ");

    for(i = 0; i < 3; i++)
    {  
        printf("%d ", arr[i]);
    }
    printf("\n");

    printf("los elementos del arreglo inverso son: ");

    for(i = 2; i >= 0; i--)
    {  
        printf("%d ", arr[i]);
    }
    printf("\n");


    return 0;

}