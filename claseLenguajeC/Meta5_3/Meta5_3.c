//Librerias
#include <stdio.h>
#include <string.h>

//Punteros de funciones

typedef int (*comparadorCadenas)(const char *, const char * );
typedef const char* (*buscadorCaracter)(const char*, char);
typedef const char* (*Subcadena)(const char*, const char*);

//Declaracion de funciones

int Com_Cadenas(const char *cadena1,const char *cadena2);
const char* Enc_caracter(const char* cadena, char caracter);
const char* Bus_subcadena(const char* cadena, const char* subcadena);

//Codigo principal
int main()
{
    char cadena1[100];
    char cadena2[100];
    char caracter;
    char opc;

    do
    {
        printf("-------------------------------------------------\n");
        printf("bienvenido al programa Meta 5.3!\n");
        printf("-------------------------------------------------\n");
        printf("[a] Comparar igualdad de dos cadenas\n[b] Priemer aparicion de un caracter\n[c] Cadena dentro de Cadena\n[d] Salir\n");
        printf("-------------------------------------------------\n");


        printf("Que deceas hacer ? ");
        scanf("%s", &opc);
        printf("-------------------------------------------------\n");
        
        switch (opc)
        {
        case 'a':

            printf("Dame la primera cadena: ");
            scanf("%s", &cadena1);
            printf("Dame la segunda cadena: ");
            scanf("%s", &cadena2);

            comparadorCadenas puntero_funcion;

            puntero_funcion = &Com_Cadenas;
            
            printf("Comparacion de las cadenas: %d\n", puntero_funcion(cadena1,cadena2));

        break;


        case 'b':

            printf("Dame la cadena: ");
            scanf("%s", cadena1);

            printf("Dame el caracter que buscas: ");
            scanf(" %c", &caracter);

            buscadorCaracter puntero_funcion2;
            
            puntero_funcion2 = &Enc_caracter;

            const char* resultado = puntero_funcion2(cadena1, caracter);

            if (resultado != NULL)
            {
                printf("El caracter '%c' fue encontrado en la cadena en la posicion: %ld\n", caracter, resultado - cadena1 + 1 );
            } 
            else 
            {
                printf("El caracter '%c' no fue encontrado en la cadena.\n", caracter);
            }


        break;

        case 'c':

            printf("Dame la primera cadena: ");
            scanf("%s", &cadena1);
            printf("Dame la segunda cadena: ");
            scanf("%s", &cadena2);

            Subcadena puntero_funcion3;

            puntero_funcion3 = &Bus_subcadena;

            const char* resultado2 = puntero_funcion3(cadena2, cadena1);

            if(resultado != NULL && strcmp(resultado2, cadena1) == 0)
            {
                printf("La subcadena '%s' fue encontrada en la cadena '%s' en la posicion: %ld\n", cadena1, cadena2, resultado2 - cadena2 + 1);
            }
            else
            {
                printf("La subcadena '%s' no fue encontrada en la cadena '%s'.\n", cadena1, cadena2);
            }
        
        break;

        }


    }

    while (opc != 'd');
    
    printf("Gracias por unar el programa, hasta luego!\n");
    printf("-------------------------------------------------\n");
    
    return 0;

}



//Funciones
int Com_Cadenas(const char *cadena1,const char *cadena2)
{

    while (*cadena1 && *cadena2 && *cadena1 == *cadena2)
    {
        cadena1++;
        cadena2++;
    }
    
    return *cadena1 - *cadena2;

}

const char* Enc_caracter(const char* cadena, char caracter)
{

    while (*cadena != '\0')
    {
        if(*cadena == caracter)
        {

            return cadena;

        }
        cadena++;
    }
    
    return NULL;

}

const char* Bus_subcadena(const char* cadena, const char* subcadena)
{

return strstr(cadena, subcadena);// la funcion strstr busca si se repite una cadena dentro de otra

}

