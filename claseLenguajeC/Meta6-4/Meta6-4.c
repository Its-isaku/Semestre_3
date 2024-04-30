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

    fptr = fopen(filename, "wb");
    if (fptr == NULL)
    {

        printf("Cannot open file\n");
        exit(0);

    }

    printf("Enter the last name: \n");
    scanf("%s", grupo.apellido);
    while(strcmp("#", grupo.apellido) != 0)
    {

        scanf("%s", grupo.nombre);
        scanf("%d", grupo.edad);
        scanf("%f", grupo.altura);
        printf("%d \n",++i);
        fwrite(&grupo, sizeof(Alumno), 1, fptr);
        printf("Enter last name: \n");
        scanf("%s", grupo.apellido);

    }

fclose(fptr);
return 0;
}