#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct
{

    unsigned int ayunas:1;

}Ayunas;

bool Fun1()
{

    char respuesta[1];

    printf("Vienes en auyunas?[s / n] ");
    scanf("%2s", respuesta);

    if (respuesta[0] == 's' || respuesta[0] == 'S')
    {
        return true;
    }

    else
    {
        return false;
    }
    
}



int main()
{

    Ayunas ayunasStatus;
    ayunasStatus.ayunas = Fun1();

    if (ayunasStatus.ayunas )
    {
        printf("Eres apto para donar sangre");
    }
    
    else
    {
        printf("Eres no apto para donar sangre");
    }
    

    return 0;
}