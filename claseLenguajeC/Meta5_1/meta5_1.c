#include <stdio.h>

int funcion(int argumento);

int main(int argc, char *argv[])
{
    int variableLocal = 33;
    int resultadoDeLlamada;

    printf("\n\nVisualización de direcciones\n\
======\n\n");
    printf("\nLa direccion de variableLocal es %p\n", (void*)&variableLocal);
    printf("La direccion de resultadoDeLlamada es %p\n", (void*)&resultadoDeLlamada);
    printf("La direccion de main es %p\n", (void*)&main);
    printf("La direccion de funcion es %p\n", (void*)&funcion);

    resultadoDeLlamada = funcion (variableLocal);

    printf("\n\nvariableLocal vale %d y resultadoDeLlamada vale %d\n", variableLocal, resultadoDeLlamada);

    return 0;
}

int funcion (int argumento) 
{
    int resultado;

    resultado = argumento * 3;

    printf("La dirección de argumento es %p\n", (void*)&argumento);
    printf("La dirección de resultado es %p\n", (void*)&resultado);

    return resultado;
}
