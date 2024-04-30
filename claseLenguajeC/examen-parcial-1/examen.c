//librerias
#include<stdio.h>
#include<math.h>
#include<string.h>

//Declaracion de funciones
void leyenda(int calificacion);
void promedio( int calificaciones[], int n);



//Codigo main
int main()
{
    char nombre[20];
    int i;
    
    printf("cuales tu Nombre: ");
    scanf("%s", nombre);
    printf("--------------------------------\n");
    
    int calificaciones[8];
    printf("dame tus 8 calificaciones:\n");
    printf("--------------------------------\n");

    for(i = 0; i < 8; i++)
    {
        printf("calificacion[%d]: ", i+1);
        scanf("%d", &calificaciones[i]); // Aquí corregido, pasando la dirección de calificaciones[i]

        leyenda(calificaciones[i]);
    }

    
    promedio(calificaciones, 8);

    return 0;
}


//Funciones
void leyenda(int calificacion)
{
    if(calificacion >= 90 && calificacion <= 100)
    {
        printf("Excelente!\n");
    }
    else if(calificacion >= 80 && calificacion <= 89)
    {
        printf("Muy bueno!\n");
    }
    else if(calificacion >= 70 && calificacion <= 79)
    {
        printf("Bueno!\n");
    }
    else if(calificacion >= 60 && calificacion <= 69)
    {
        printf("Regular!\n");
    }
    else if(calificacion >= 0 && calificacion <= 59)
    {
        printf("Insuficiente!\n");
    }
    else
    {
        printf("Calificación no válida\n");
    }
    
    printf("--------------------------------\n");
}


void promedio( int calificaciones[], int n)
{

    int suma = 0;

    for(int i = 0; i < n; i++)
    {
        suma += calificaciones[i];
    }

    double promedio = (double)suma/n;

    printf("Promedio: %.2f", promedio);
    leyenda((int)promedio);

}

