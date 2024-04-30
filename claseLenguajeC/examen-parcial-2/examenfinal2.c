//Librerias
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Estructuras
typedef struct Nodo
{
    char *ID;
    char *Estatus;
    char *Lab;
    char *Marca;
    char *Modelo;
    char *Anio;
    char *IP;
    char *SO;
    struct Nodo *sig;
} Nodo;

typedef Nodo *NodoRef;
//funciones
void mostrarLista(NodoRef);
void agregarCompu(NodoRef *, char *, char *, char *, char *, char *, char *, char *, char *);
void borrarCompu(NodoRef *, char *);
void ModificarCompu(NodoRef *, char *);

//codigo principal
int main()
{

    NodoRef listaCompus = NULL;
    char opcion;

    do
    {
        //menu de opciones
        printf("******************************************************\n");
        printf("*                                                    *\n");
        printf("*             [1] Agregar Computadora                *\n");
        printf("*             [2] Mostrar Lista de computadoras      *\n");
        printf("*             [3] Modificar Estatus                  *\n");
        printf("*             [4] salir                              *\n");
        printf("*                                                    *\n");
        printf("******************************************************\n");
        printf("Ingrese una opcion: ");
        scanf(" %c", &opcion);
        printf("------------------------------------------------------\n");

        switch (opcion)
        {

        //Agregar computadora
        case '1':
        {
            char ID[50], Estatus[20], Lab[20], Marca[50], Modelo[50], Anio[10], IP[20], SO[20];
            printf("Ingrese ID: ");
            scanf(" %[^\n]", ID);
            printf("Ingrese Estatus(Activo/Inactivo): ");
            scanf(" %[^\n]", Estatus);// el " %[^\n]" me permta dar un string con espacios entre palabras
            printf("Ingrese Lab: ");
            scanf(" %[^\n]", Lab);
            printf("Ingrese Marca: ");
            scanf(" %[^\n]", Marca);
            printf("Ingrese Modelo: ");
            scanf(" %[^\n]", Modelo);
            printf("Ingrese Anio: ");
            scanf(" %[^\n]", Anio);
            printf("Ingrese IP: ");
            scanf(" %[^\n]", IP);
            printf("Ingrese SO: ");
            scanf(" %[^\n]", SO);
            printf("------------------------------------------------------\n");
            agregarCompu(&listaCompus, ID, Estatus, Lab, Marca, Modelo, Anio, IP, SO);
            break;
        }

        //Mostrar lista de Computadoras
        case '2':
            printf("\nContenido de la lista de Compuatadoras:\n");
            mostrarLista(listaCompus);
            break;

        case '3':
        char ID[50];
            printf("Ingresa el ID de la computadora que deseas modificar? \n");
            scanf(" %[^\n]", ID);
            printf("------------------------------------------------------\n");
            ModificarCompu(&listaCompus, ID);
            break;

        //Salir
        case '4':
            printf("Gracias por usar el programa, hasta luego!.\n");
            printf("------------------------------------------------------\n");
            break;

        //Opcion invalida
        default:
            printf("Opcion no valida. Por favor, seleccione una opcion valida.\n");
            printf("------------------------------------------------------\n");
            break;
        }

    } while (opcion != '4');

    return 0;
}

void mostrarLista(NodoRef NodoIni)
{
    NodoRef Computadora;
    printf("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n");
    printf("PUNTERO                          ID          Estatus                       Lab               Marca                  Modelo                  Anio                  IP                         SO                SIGUIENTE                     |\n");
    printf("\n");
    for (Computadora = NodoIni; Computadora != NULL; Computadora = Computadora->sig)
    {
        printf("Puntero = %4p       ID = %s       Estatus = %s               Lab = %s          Marca = %s          Modelo = %s          Anio = %s          IP = %s          SO = %s          sig = %4p       |\n", Computadora, Computadora->ID, Computadora->Estatus, Computadora->Lab, Computadora->Marca, Computadora->Modelo, Computadora->Anio, Computadora->IP, Computadora->SO, Computadora->sig);
    }
    printf("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n");
}

void agregarCompu(NodoRef *lista, char *ID, char *Estatus, char *Lab, char *Marca, char *Modelo, char *Anio, char *IP, char *SO)
{
    NodoRef NuevaCompu = (NodoRef)malloc(sizeof(Nodo));
    NuevaCompu->ID = strdup(ID);
    NuevaCompu->ID = strdup(ID);
    NuevaCompu->Estatus = strdup(Estatus);
    NuevaCompu->Lab = strdup(Lab);
    NuevaCompu->Marca = strdup(Marca);
    NuevaCompu->Modelo = strdup(Modelo);
    NuevaCompu->Anio = strdup(Anio);
    NuevaCompu->IP = strdup(IP);
    NuevaCompu->SO = strdup(SO);
    NuevaCompu->sig = NULL;

    if (*lista == NULL)
    {
        *lista = NuevaCompu;
    }
    else
    {
        NodoRef ultimo = *lista;
        while (ultimo->sig != NULL)
        {
            ultimo = ultimo->sig;
        }
        ultimo->sig = NuevaCompu;
    }
}

void ModificarCompu(NodoRef *lista, char *ID)
{

    NodoRef actual = *lista;
    int encontrado = 0; 
    char opc;
    char nuevoEstatus[50];

    //buscar Computadora por ID 
    while (actual!= NULL && !encontrado)
    {
    
        if (strcmp(actual -> ID , ID) == 0)
        {

            encontrado = 1;
            break;

        }

        actual = actual -> sig;

    }

    if (!encontrado)
    {

        printf("Computadora no encontrada.\n");
        return;

    }

    printf("Ingrese el nuevo Estatus: \n");
    scanf(" %[^\n]", nuevoEstatus); // Leer el nuevo Estatus
    printf("------------------------------------------------------\n");
    //Libera la memoria del nombre actual
        free(actual -> Estatus);
        //asigno nuevo nombre
        actual -> Estatus = strdup(nuevoEstatus);
}

