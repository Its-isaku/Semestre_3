#include <stdio.h>

//funciones de operaciones

int suma(int x, int y);
int resta(int x, int y);
int mult(int x, int y);
float div(int x, int y);

//codigo main
int main()
{

    int opc;

    do
    {

    printf("Bienvenido a la calculadora!\nQue operacion deceas realizar?\n");
    printf("-------------------------------------------------------------\n");
    printf("[1]suma\n[2]resta\n[3]multiplicacion\n[4]division\n[5]salir\n");
    scanf("%d", &opc);
    printf("-------------------------------------------------------------\n");

        int a, b;
        switch(opc)

        {

            case 1:

            printf("Dame el primer valor a sumar: ");
            scanf("%d", &a);

            printf("Dame el segundo valor a sumar: ");
            scanf("%d", &b);

            printf("el resultado es %d\n",suma(a, b));
            printf("-------------------------------------------------------------\n");

            break;

            //-----------------------------------

            case 2:

            printf("Dame el primer valor a restar: ");
            scanf("%d", &a);

            printf("Dame el segundo valor a restar: ");
            scanf("%d", &b);

            printf("el resultado es %d\n", resta(a, b));
            printf("-------------------------------------------------------------\n");

            break;

            //-----------------------------------

            case 3:

            printf("Dame el primer valor a Multiplicar: ");
            scanf("%d", &a);

            printf("Dame el segundo valor a Multiplicar: ");
            scanf("%d", &b);

            printf("el resultado es %d\n", mult(a, b));
            printf("-------------------------------------------------------------\n");

            break;

            //-----------------------------------

            case 4:

            printf("Dame el primer valor a dividir: ");
            scanf("%d", &a);

            printf("Dame el segundo valor a dividir: ");
            scanf("%d", &b);

            printf("el resultado es %.2f\n", div(a, b));
            printf("-------------------------------------------------------------\n");

            break;

            //-----------------------------------

            default:

            break;

        }

        

    }while (opc != 5);


    printf("Gracias por usar el programa, haasta luego!!\n");
    printf("-------------------------------------------------------------\n");

    return 0;

}

//funciones


int suma(int x, int y)
{
    int resultadoS = x + y;

    return resultadoS;

}

int resta(int x, int y)
{
    int resultadoR = x - y;

    return resultadoR;

}

int mult(int x, int y)
{
    int resultadoM = x * y;

    return resultadoM;

}

float div(int x, int y)
{
    float resultadoD = x / y;

    return resultadoD;
}