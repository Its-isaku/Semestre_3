#include<stdio.h>

int main()
{
    int arr1[3];
    int arr2[3];
    int i;

    for(i = 0; i < 3; i++)
    {
        printf("Dame el valor del arreglo [%d]: ", i);
        scanf("%d", &arr1[i]);
    }

    printf("Los elementos del primer arreglo son: ");
    for(i = 0; i < 3; i++)
    {
        printf("%d ", arr1[i]);
    }
    printf("\n");
    
    for(i = 0; i < 3; i++)
    {

        arr2[i] = arr1[i];

    }


    printf("Los elementos del segundo arreglo son: ");
    for(i = 0; i < 3; i++)
    {
        printf("%d ", arr2[i]);
    }
    printf("\n");

    return 0; 

}