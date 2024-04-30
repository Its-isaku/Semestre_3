#include <stdio.h>
#include <stdlib.h> 
#include <string.h>

typedef struct
{

    char apellido [30];
    char nombre [15];
    int edad;
    float altura;

} Alumno;


int main()
{

    FILE *fptr;
    Alumno grupo;
    
    char filename[100], c;
    int i = 0;

    printf("Enter the filename to open: \n");
    scanf("%s", filename);

    fptr = fopen(filename, "rb");
    if (fptr == NULL)
    {

        printf("Cannot open file\n");
        exit(0);

    }

    printf("Enter position: \n");
    scanf("%s", &i);
    fseek(fptr,(i-1)*(sizeof(Alumno)), 0);
    fread(&grupo, sizeof(Alumno), 1, fptr);
    printf("Apellido: %s\n", grupo.apellido);
    printf("nombre: %s\n", grupo.nombre);
    printf("edad: %s\n", grupo.edad);
    printf("altura: %s\n", grupo.altura);


fclose(fptr);
return 0;
}