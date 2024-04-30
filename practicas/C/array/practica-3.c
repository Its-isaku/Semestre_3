#include<stdio.h>

int main()
{

    int arr[3];
    int i;
    int sum = 0;

    for(i = 0; i < 3; i++)
    {
        printf("Dame le valor del arreglo[%d]: ", i+1);
        scanf("%d", &arr[i]);
    }

    for(i = 0; i < 3; i++)
    {
        sum += arr[i];
    }
    printf(" la suma de los arreglos es: %d", sum);

    return 0;

}