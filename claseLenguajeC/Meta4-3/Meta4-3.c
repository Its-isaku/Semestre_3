#include <stdio.h>


//Declaracion de funciones
int Buscador(int arr[], int n, int num);
void bubbleSort(int arr[], int n);
float mediana(int arr[], int n);
float media (int arr[], int n);


//Codigo principal
int main ()
{


    int n, num, Num_encontrado;


    printf("Dame el largo del arreglo: ");
    scanf("%d", &n);
    printf("---------------------------------------\n");


    int arr[n];


    printf("Dame los valores del arreglo: \n");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    printf("---------------------------------------\n");


    bubbleSort(arr,n);


    printf("El arreglo ordenado es: ");
    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }


    printf("\n");
    printf("---------------------------------------\n");


    printf("La mediana del arreglo es : %.2f\n", mediana(arr, n));
    ("---------------------------------------\n");
    printf("La media del arreglo es : %.2f\n", media(arr, n));
    printf("---------------------------------------\n");


    printf("Que numero deseas bucar en el arreglo: ");
    scanf("%d", &num);
    printf("---------------------------------------\n");
    Num_encontrado = Buscador(arr, n, num);
    printf("El numero %d se repite %d veces en el arreglo\n", num, Num_encontrado);
    printf("---------------------------------------\n");
    printf("Gracias por usar el programa, hasta luego!\n");
    printf("---------------------------------------\n");


    return 0;


}


//Funciones


void bubbleSort(int arr[], int n)
{


    int i, j, temp;
    for(i = 0; i < n; i++)
    {
        for(j = 0; j < n-i-1; j++)
        {
            if( arr[j] > arr[j+1])
            {
                //Intercambia las variables
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }


}




float mediana(int arr[], int n)
{
    if(n % 2 != 0)
    {
        return arr[n/2];
    }
    else
    {
        return (arr[n / 2 - 1] + arr[n/2]) / 2.0;
    }
}




float media (int arr[], int n)
{
    float sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += arr[i];
    }
    return sum / n;
}




int Buscador(int arr[], int n, int num)
{
    int countador = 0;
    for (int i = 0; i < n; i++)
    {
        if(arr[i] == num)
        {
            countador++;
        }
    }
   
    return countador;
}
