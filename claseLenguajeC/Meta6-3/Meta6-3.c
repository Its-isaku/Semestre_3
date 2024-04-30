#include <stdio.h>
#include <stdlib.h>


typedef struct Nodo
{

    int valor;
    struct Nodo* sig;

} Nodo;

typedef Nodo* NodoRef;

void mostrarLista(NodoRef);

int main()
{

    NodoRef p1 = (Nodo*)malloc(sizeof(Nodo));
    NodoRef p2 = (Nodo*)malloc(sizeof(Nodo));
    NodoRef p3 = (Nodo*)malloc(sizeof(Nodo));
    NodoRef p4 = (Nodo*)malloc(sizeof(Nodo));

    p1 -> valor = 1;
    p1 -> sig = p2;
    p2 -> valor = 2;
    p2 -> sig = p3;
    p3 -> valor = 3;
    p4 -> sig = p4;
    p4 -> valor = 4;
    p4 -> sig = NULL;

    printf("\nContenido de una liste simple enlazada\n");

    mostrarLista(p1);

    return 0;
}

void mostrarLista(NodoRef NodoIni)
{

    NodoRef p;
    printf("\n-------------------------------------------------------------------------------------\n");
    printf("PUNTERO                    VALOR                    SIGUIENTE                       |\n");
    printf("\n");
    for(p = NodoIni; p != NULL;p = p->sig)
        printf("p = %8p       p->valor = %4d          p->sig = %8p       |\n", p, p -> valor, p -> sig);
        printf("\n-------------------------------------------------------------------------------------\n");



}