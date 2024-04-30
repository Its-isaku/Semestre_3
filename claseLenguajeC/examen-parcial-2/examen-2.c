//Librerias
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


//Estructuras
typedef struct Nodo
{
    char *nombre;
    char *numero;
    char *codigoPostal;
    char *colonia;
    char *calle;
    struct Nodo *sig;
} Nodo;

typedef Nodo *NodoRef;
//funciones
void mostrarLista(NodoRef);
void agregarContacto(NodoRef *, char *, char *, char *, char *, char *);
void borrarContacto(NodoRef *, char *);
void ModificarContacto(NodoRef *, char *);

//codigo principal
int main()
{

    NodoRef listaContactos = NULL;
    char opcion;

    do
    {
        //menu de opciones
        printf("******************************************************\n");
        printf("*                                                    *\n");
        printf("*             [1] Agregar contacto                   *\n");
        printf("*             [2] Borrar Contacto                    *\n");
        printf("*             [3] Mostrar Lista de contactos         *\n");
        printf("*             [4] Modificar                          *\n");
        printf("*             [5] salir                              *\n");
        printf("*                                                    *\n");
        printf("******************************************************\n");
        printf("Ingrese una opcion: ");
        scanf(" %c", &opcion);
        printf("------------------------------------------------------\n");

        switch (opcion)
        {

        //Agregar contacto
        case '1':
        {
            char nombre[50], numero[20], codigoPostal[10], colonia[50], calle[50];
            printf("Ingrese nombre: ");
            scanf(" %[^\n]", nombre); // el " %[^\n]" me permta dar un string con espacios entre palabras
            printf("Ingrese numero: ");
            scanf(" %[^\n]", numero);
            printf("Ingrese codigo postal: ");
            scanf(" %[^\n]", codigoPostal);
            printf("Ingrese colonia: ");
            scanf(" %[^\n]", colonia);
            printf("Ingrese calle: ");
            scanf(" %[^\n]", calle);
            printf("------------------------------------------------------\n");
            agregarContacto(&listaContactos, nombre, numero, codigoPostal, colonia, calle);
            break;
        }

        //Borrar contacto
        case '2':
        {
            char nombre[50];
            printf("Ingrese nombre del contacto a borrar: ");
            scanf(" %[^\n]", nombre);
            printf("------------------------------------------------------\n");
            borrarContacto(&listaContactos, nombre);
            break;
        }

        //Mostrar lista de contactos
        case '3':
            printf("\nContenido de la lista de contactos:\n");
            mostrarLista(listaContactos);
            break;

        case '4':
        char nombre[50];
            printf("Que contacto deseas modificar? \n");
            scanf(" %[^\n]", nombre);
            printf("------------------------------------------------------\n");
            ModificarContacto(&listaContactos, nombre);
            break;

        //Salir
        case '5':
            printf("Gracias por usar el programa, hasta luego!.\n");
            printf("------------------------------------------------------\n");
            break;

        //Opcion invalida
        default:
            printf("Opcion no valida. Por favor, seleccione una opcion valida.\n");
            printf("------------------------------------------------------\n");
            break;
        }

    } while (opcion != '5');

    return 0;
}

void mostrarLista(NodoRef NodoIni)
{
    NodoRef contacto;
    printf("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n");
    printf("PUNTERO                           NOMBRE                      NUMERO                       CODIGO POSTAL                  COLONIA                    CALLE                   SIGUIENTE                     |\n");
    printf("\n");
    for (contacto = NodoIni; contacto != NULL; contacto = contacto->sig)
    {
        printf("contacto = %4p       nombre = %s               numero = %s          codigo postal = %s          colonia = %s          calle = %s          sig = %4p       |\n", contacto, contacto->nombre, contacto->numero, contacto->codigoPostal, contacto->colonia, contacto->calle, contacto->sig);
    }
    printf("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n");
}

void agregarContacto(NodoRef *lista, char *nombre, char *numero, char *codigoPostal, char *colonia, char *calle)
{
    NodoRef nuevoContacto = (NodoRef)malloc(sizeof(Nodo));
    nuevoContacto->nombre = strdup(nombre);
    nuevoContacto->numero = strdup(numero);
    nuevoContacto->codigoPostal = strdup(codigoPostal);
    nuevoContacto->colonia = strdup(colonia);
    nuevoContacto->calle = strdup(calle);
    nuevoContacto->sig = NULL;

    if (*lista == NULL)
    {
        *lista = nuevoContacto;
    }
    else
    {
        NodoRef ultimo = *lista;
        while (ultimo->sig != NULL)
        {
            ultimo = ultimo->sig;
        }
        ultimo->sig = nuevoContacto;
    }
}

void borrarContacto(NodoRef *lista, char *nombre)
{
    NodoRef actual = *lista;
    NodoRef anterior = NULL;

    while (actual != NULL && strcmp(actual->nombre, nombre) != 0)
    {
        anterior = actual;
        actual = actual->sig;
    }

    if (actual == NULL)
    {
        printf("No se encontró el contacto con el nombre %s\n", nombre);
        return;
    }

    if (anterior == NULL)
    {
        *lista = actual->sig;
    }
    else
    {
        anterior->sig = actual->sig;
    }

    free(actual->nombre);
    free(actual->numero);
    free(actual->codigoPostal);
    free(actual->colonia);
    free(actual->calle);
    free(actual);
}

void ModificarContacto(NodoRef *lista, char *nombre)
{

    NodoRef actual = *lista;
    int encontrado = 0; 
    char opc;
    char nuevoValor[50];

    //buscar el contacto por nombre
    while (actual!= NULL && !encontrado)
    {
    
        if (strcmp(actual -> nombre , nombre) == 0)
        {

            encontrado = 1;
            break;

        }

        actual = actual -> sig;

    }

    if (!encontrado)
    {

        printf("contacto no encontrado.\n");
        return;

    }

    //Mostrar opciones de Modificacion
    printf("******************************************************\n");
    printf("*                                                    *\n");
    printf("*             [1] Nombre                             *\n");
    printf("*             [2] Numero                             *\n");
    printf("*             [3] Codigo Postal                      *\n");
    printf("*             [4] Colonia                            *\n");
    printf("*             [5] Calle                              *\n");
    printf("*                                                    *\n");
    printf("******************************************************\n");
    printf("Que deceas modificar: \n");
    scanf(" %c", &opc);
    printf("------------------------------------------------------\n");

    switch (opc)
    {

        case '1':
        printf("Ingrese el nuevo valor: \n");
        scanf(" %[^\n]", nuevoValor); // Leer el nuevo valor
        printf("------------------------------------------------------\n");
        //Libera la memoria del nombre actual
            free(actual -> nombre);
            //asigno nuevo nombre
            actual -> nombre = strdup(nuevoValor);
            break;

        case '2':
        printf("Ingrese el nuevo valor: \n");
        scanf(" %[^\n]", nuevoValor); // Leer el nuevo valor
        printf("------------------------------------------------------\n");
        //Libera la memoria del numero actual
            free(actual -> numero);
            //asigno nuevo numero
            actual -> numero = strdup(nuevoValor);
            break;

        case '3':
        printf("Ingrese el nuevo valor: \n");
        scanf(" %[^\n]", nuevoValor); // Leer el nuevo valor
        printf("------------------------------------------------------\n");
        //Libera la memoria del codigoPostal actual
            free(actual -> codigoPostal);
            //asigno nuevo codigoPostal
            actual -> codigoPostal = strdup(nuevoValor);
            break;

        case '4':
        printf("Ingrese el nuevo valor: \n");
        scanf(" %[^\n]", nuevoValor); // Leer el nuevo valor
        printf("------------------------------------------------------\n");
        //Libera la memoria del colonia actual
            free(actual -> colonia);
            //asigno nuevo colonia
            actual -> colonia = strdup(nuevoValor);
            break;

        case '5':
        printf("Ingrese el nuevo valor: \n");
        scanf(" %[^\n]", nuevoValor); // Leer el nuevo valor
        printf("------------------------------------------------------\n");
        //Libera la memoria del calle actual
            free(actual -> calle);
            //asigno nuevo calle
            actual -> calle = strdup(nuevoValor);
            break;

        default:
            printf("Opcion no valida. Por favor, seleccione una opcian valida.\n");
            printf("------------------------------------------------------\n");
            break;


    }

    if(encontrado)
    {
        printf("contacto modificado exitosamente! \n");
    }

}               

