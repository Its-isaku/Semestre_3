//Librerias
#include <stdio.h>
#include <stdlib.h>


//Declaracion de funciones


//codigo main

int main() 
{
    int N, M;
    printf("Dame los valores de la matriz (NxM): ");
    scanf("%d %d", &N, &M);

    //pedir memoria con malloc
    double* matrix = malloc(N*M*sizeof(double));

    //mostrarel resltado
    for(int i = 0; i < N; i++)
    {

        for(int j = 0; j < M; j++)
        {
            int indice = i * M + j;
            double* direcion = &matrix[indice];
            printf("Los elementos ( %d. %d) tienen la direccion: %p y el indice; %d \n", i, j, direcion, indice + 1);
        }

    }

    //liberer memoria
    free(matrix);

    return 0;

}
