#include <stdio.h>
#include <stdlib.h>


typedef struct Nodo
{

    char* nombre;
    char* numero;
    struct Nodo* sig;

} Nodo;

typedef Nodo* NodoRef;

void mostrarLista(NodoRef);

int main()
{

    NodoRef contacto1 = (Nodo*)malloc(sizeof(Nodo));
    NodoRef contacto2 = (Nodo*)malloc(sizeof(Nodo));
    NodoRef contacto3 = (Nodo*)malloc(sizeof(Nodo));
    NodoRef contacto4 = (Nodo*)malloc(sizeof(Nodo));

    contacto1 -> nombre = "Isai";
    contacto1 -> numero = "6651272501";
    contacto1 -> sig = contacto2;
    contacto2 -> nombre = "Aaron";
    contacto2 -> numero = "6651270811";
    contacto2 -> sig = contacto3;
    contacto3 -> nombre = "Abel";
    contacto3 -> numero = "6651270520";
    contacto3 -> sig = contacto4;
    contacto4 -> nombre = "Alejandra";
    contacto4 -> numero = "6651272495";
    contacto4 -> sig = NULL;

    printf("\nContenido de una liste simple enlazada\n");

    mostrarLista(contacto1);

    return 0;
}

void mostrarLista(NodoRef NodoIni)
{

    NodoRef contacto;
    printf("\n-------------------------------------------------------------------------------------\n");
    printf("PUNTERO                           NOMBRE                                NUMERO                                 SIGUIENTE                                   |\n");
    printf("\n");
    for(contacto = NodoIni; contacto != NULL;contacto = contacto->sig)
        printf("contacto = %8p       contacto->nombre = %s               contacto->numero = %s          contacto->sig = %8p       |\n", contacto, contacto -> nombre, contacto -> numero, contacto -> sig);
        printf("\n-------------------------------------------------------------------------------------\n");



}