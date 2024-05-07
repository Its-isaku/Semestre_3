//Declaracion de librerias
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

//Declaracion de funciones
void bubbleSort(int arr[], int n);
float mediana(int arr[], int n);
float media(int arr[], int n);
float media_recortada(int arr[], int n, float porcentaje);
float moda(int arr[], int n);
float varianza_for1(int arr[], int n, float media, int *contador);
float varianza_for2(int arr[], int n, float media, int *contador);
double calcular_tiempo(struct timespec start, struct timespec end);

double Calc_Z(double Alpha);

double Calc_T(double Alpha, int NivSig);


//codigo main
int main()
{

    int opc;

    do
    {   
        
        struct timespec start, end;
        double tiempo_formula1, tiempo_formula2;

        printf("------------------------------------------------------\n");
        printf("Bienvendo alproyecto final de estadistica!\n");
        printf("------------------------------------------------------\n");
        printf("\n");
        printf("----------rutinas para graficos----------\n");
        printf("[1]Tallos y hojas........................\n[2]Grafa de puntos.......................\n[3]Histograma............................\n[4]Estadicos.............................\n");
        printf("\n");
        printf("----------rutinas para calcular----------\n");
        printf("[5]Moda..................................\n[6]Media.................................\n[7]Media recortada.......................\n[8]Mediana...............................\n");
        printf("[9]Varianza y desviacion estandar........\n");
        printf("\n");
        printf("--------rutinas para Tablas(Z y T)-------\n");
        printf("[10]Calcular valores alha(tabla Z).......\n[11]Encontrar Z con alpha................\n[12]Localizar T..........................\n[13]Localizar grados de libertad y T.....\n");
        printf("\n");
        printf("--------------Otras opciones-------------\n");
        printf("[0]salir....................\n");
        printf("\n");
        printf("------------------------------------------------------\n");
        printf("Que deceas hacer? ");
        scanf("%d", &opc);
        printf("------------------------------------------------------\n");

        int n;
        int *arr;
        float porcentaje;

        switch (opc)
        {
                
            case 1: //Tallos y hojas - Despues
                
            break;

            //-----------------------------------------------

            case 2: //Grafica de puntos - Despues
                
            break;

            //-----------------------------------------------

            case 3: //Histograma - Despues
                
            break;

            //-----------------------------------------------

            case 4: //Estadicos - Despues
                
            break;

            //-----------------------------------------------

            case 5: // Moda
            case 6: // Media
            case 8: // Mediana

            int opc2;
            printf("Quieres leer los datos de un archivo o propocionarlos tu?\n---------------------------------------\n[1] De un archivo\n[2] Dar los datos\n---------------------------------------\n");
            scanf("%d", &opc2);
            printf("---------------------------------------\n");

            if(opc2 == 2)
            {

                printf("Dame el largo del arreglo: ");
                scanf("%d", &n);
                printf("---------------------------------------\n");

                if (n <= 0)
                {
                    printf("El tamaño del arreglo debe ser mayor que 0.\n");
                    continue;
                }

                // Asignación dinámica de memoria para el arreglo
                arr = (int *)malloc(n * sizeof(int));

                if (arr == NULL)
                {
                    printf("Error al asignar memoria.\n");
                    return 1;
                }

                printf("Dame los valores del arreglo: \n");
                for (int i = 0; i < n; i++)
                {
                    scanf("%d", &arr[i]);
                }
                printf("---------------------------------------\n");

                bubbleSort(arr, n);

                printf("El arreglo ordenado es: ");
                for (int i = 0; i < n; i++)
                {
                    printf("%d ", arr[i]);
                }
                printf("\n");
                printf("---------------------------------------\n");

                switch (opc)
                {
                case 5: // Moda
                    printf("La moda del arreglo es : %.2f\n", moda(arr, n));
                    break;

                case 6: // Media
                    printf("La media del arreglo es : %.2f\n", media(arr, n));
                    break;

                case 8: // Mediana
                    printf("La mediana del arreglo es : %.2f\n", mediana(arr, n));
                    break;
                }

                // Liberar la memoria asignada
                free(arr);
                break;

                //-----------------------------------------------
            
            }
            else
            {
                int total;
                FILE *arch;
                arch = fopen("prueba.txt", "r");
                if(arch != NULL)
                {

                    fscanf(arch, "%d", &total);
                // Asignación dinámica de memoria para el arreglo
                arr = (int *)malloc(total * sizeof(int));
                if (arr == NULL)
                {
                    printf("Error al asignar memoria!\n");
                    return 1;
                }

                for(int i = 0; i < total; i++)
                {
                    fscanf(arch, "%d", &arr[i]);
                }
                fclose(arch);
                n = total;

                }
                else
                {
                    printf("el archivo no existe\n");
                    return 1;
                }

                printf("---------------------------------------\n");

                bubbleSort(arr, n);

                printf("El arreglo ordenado es: ");
                for (int i = 0; i < n; i++)
                {
                    printf("%d ", arr[i]);
                }
                printf("\n");
                printf("---------------------------------------\n");

                switch (opc)
                {
                case 5: // Moda
                    printf("La moda del arreglo es : %.2f\n", moda(arr, n));
                    break;

                case 6: // Media
                    printf("La media del arreglo es : %.2f\n", media(arr, n));
                    break;

                case 8: // Mediana
                    printf("La mediana del arreglo es : %.2f\n", mediana(arr, n));
                    break;
                }

                // Liberar la memoria asignada
                free(arr);
                break;

            }

            //-----------------------------------------------

            case 7: // Media recortada

            int opc3;
            printf("Quieres leer los datos de un archivo o propocionarlos tu?\n---------------------------------------\n[1] De un archivo\n[2] Dar los datos\n---------------------------------------\n");
            scanf("%d", &opc3);

            if(opc3 == 2)
            {
                printf("Dame el largo del arreglo: ");
                scanf("%d", &n);
                printf("---------------------------------------\n");

                if (n <= 0) {
                    printf("El tamaño del arreglo debe ser mayor que 0.\n");
                    continue;
                }

                // Asignación dinámica de memoria para el arreglo
                arr = (int *)malloc(n * sizeof(int));

                if (arr == NULL) {
                    printf("Error al asignar memoria.\n");
                    return 1;
                }

                printf("Dame los valores del arreglo: \n");
                for (int i = 0; i < n; i++) {
                    scanf("%d", &arr[i]);
                }
                printf("---------------------------------------\n");

                bubbleSort(arr, n);

                printf("Que porcentaje deseas recortar? (0.0 -> 1.0) ");
                scanf("%f", &porcentaje);
                printf("---------------------------------------\n");

                printf("El arreglo ordenado es: ");
                for (int i = 0; i < n; i++) 
                {
                    printf("%d ", arr[i]);
                }

                printf("\n");
                printf("---------------------------------------\n");
                printf("La media recortada del arreglo es : %.2f\n", media_recortada(arr, n, porcentaje));

            }
            else
            {

                int total;
                FILE *arch;
                arch = fopen("prueba.txt", "r");
                if(arch != NULL)
                {

                    fscanf(arch, "%d", &total);
                // Asignación dinámica de memoria para el arreglo
                arr = (int *)malloc(total * sizeof(int));
                if (arr == NULL)
                {
                    printf("Error al asignar memoria!\n");
                    return 1;
                }

                for(int i = 0; i < total; i++)
                {
                    fscanf(arch, "%d", &arr[i]);
                }
                fclose(arch);
                n = total;

                }
                else
                {
                    printf("el archivo no existe\n");
                    return 1;
                }

                bubbleSort(arr, n);

                printf("Que porcentaje deseas recortar? (0.0 -> 1.0) ");
                scanf("%f", &porcentaje);
                printf("---------------------------------------\n");

                printf("El arreglo ordenado es: ");
                for (int i = 0; i < n; i++) 
                {
                    printf("%d ", arr[i]);
                }

                printf("\n");
                printf("---------------------------------------\n");
                printf("La media recortada del arreglo es : %.2f\n", media_recortada(arr, n, porcentaje));

            }

            // Liberar la memoria asignada
            free(arr);
            break;

            //-----------------------------------------------

            case 9: //Varianza y Desviacion estandar
                
            int opc4;
            printf("Quieres leer los datos de un archivo o propocionarlos tu?\n---------------------------------------\n[1] De un archivo\n[2] Dar los datos\n---------------------------------------\n");
            scanf("%d", &opc4);

            if(opc4 == 2)
            {
                printf("Dame el largo del arreglo: ");
                scanf("%d", &n);
                printf("---------------------------------------\n");

                if (n <= 0) {
                    printf("El tamaño del arreglo debe ser mayor que 0.\n");
                    continue;
                }

                
                arr = (int *)malloc(n * sizeof(int));

                if (arr == NULL) {
                    printf("Error al asignar memoria.\n");
                    return 1;
                }

                printf("Dame los valores del arreglo: \n");
                for (int i = 0; i < n; i++) {
                    scanf("%d", &arr[i]);
                }
                printf("---------------------------------------\n");

                bubbleSort(arr, n);

                clock_t inicio, fin;
                double tiempo_formula1, tiempo_formula2;

                inicio = clock();
                float Media = media(arr, n);
                fin = clock();
                tiempo_formula1 = (double)(fin - inicio) / CLOCKS_PER_SEC;

                int num_calculos_formula1 = 0;
                clock_gettime(CLOCK_MONOTONIC, &start);
                float varianza1 = varianza_for1(arr, n, Media, &num_calculos_formula1);
                clock_gettime(CLOCK_MONOTONIC, &end);
                tiempo_formula1 = calcular_tiempo(start, end);

                int num_calculos_formula2 = 0;
                clock_gettime(CLOCK_MONOTONIC, &start);
                float varianza2 = varianza_for2(arr, n, Media, &num_calculos_formula2);
                clock_gettime(CLOCK_MONOTONIC, &end);
                tiempo_formula2 = calcular_tiempo(start, end);


                printf("El arreglo ordenado es: ");
                for (int i = 0; i < n; i++) 
                {
                    printf("%d ", arr[i]);
                }

                printf("\n");

                printf("---------------------------------------\n");
                printf("\nVarianza (Formula 1): %.2f\n", varianza1);
                printf("Desviacion estandar (Formula 1): %.2f\n", sqrt(varianza1));
                printf("Numero de calculos (Formula 1): %d\n", num_calculos_formula1);
                printf("Tiempo de ejecucion (Formula 1): %.10f segundos\n", tiempo_formula1);

                printf("---------------------------------------\n");

                printf("\nVarianza (Formula 2): %.2f\n", varianza2);
                printf("Desviacion estandar (Formula 2): %.2f\n", sqrt(varianza2));
                printf("Numero de calculos (Formula 2): %d\n", num_calculos_formula2);
                printf("Tiempo de ejecucion (Formula 2): %.10f segundos\n", tiempo_formula2);

            }
            else
            {

                int total;
                FILE *arch;
                arch = fopen("prueba.txt", "r");
                if(arch != NULL)
                {

                    fscanf(arch, "%d", &total);
                // Asignación dinámica de memoria para el arreglo
                arr = (int *)malloc(total * sizeof(int));
                if (arr == NULL)
                {
                    printf("Error al asignar memoria!\n");
                    return 1;
                }

                for(int i = 0; i < total; i++)
                {
                    fscanf(arch, "%d", &arr[i]);
                }
                fclose(arch);
                n = total;

                }
                else
                {
                    printf("el archivo no existe\n");
                    return 1;
                }

                bubbleSort(arr, n);

                clock_t inicio, fin;
                double tiempo_formula1, tiempo_formula2;

                inicio = clock();
                float Media = media(arr, n);
                fin = clock();
                tiempo_formula1 = (double)(fin - inicio) / CLOCKS_PER_SEC;

                int num_calculos_formula1 = 0;
                clock_gettime(CLOCK_MONOTONIC, &start);
                float varianza1 = varianza_for1(arr, n, Media, &num_calculos_formula1);
                clock_gettime(CLOCK_MONOTONIC, &end);
                tiempo_formula1 = calcular_tiempo(start, end);

                int num_calculos_formula2 = 0;
                clock_gettime(CLOCK_MONOTONIC, &start);
                float varianza2 = varianza_for2(arr, n, Media, &num_calculos_formula2);
                clock_gettime(CLOCK_MONOTONIC, &end);
                tiempo_formula2 = calcular_tiempo(start, end);
                
                printf("El arreglo ordenado es: ");
                for (int i = 0; i < n; i++) 
                {
                    printf("%d ", arr[i]);
                }
                printf("\n");

                printf("---------------------------------------\n");
                printf("\nVarianza (Formula 1): %.2f\n", varianza1);
                printf("Desviacion estandar (Formula 1): %.2f\n", sqrt(varianza1));
                printf("Numero de calculos (Formula 1): %d\n", num_calculos_formula1);
                printf("Tiempo de ejecucion (Formula 1): %.10f segundos\n", tiempo_formula1);

                printf("---------------------------------------\n");

                printf("\nVarianza (Formula 2): %.2f\n", varianza2);
                printf("Desviacion estandar (Formula 2): %.2f\n", sqrt(varianza2));
                printf("Numero de calculos (Formula 2): %d\n", num_calculos_formula2);
                printf("Tiempo de ejecucion (Formula 2): %.10f segundos\n", tiempo_formula2);

            }

            break;

            //-----------------------------------------------

            case 10: //Calcular valores alha(tabla Z y graficar area bajo la curva) - Despues


                
            break;

            //-----------------------------------------------

            case 11: //Encontrar Z con alpha y el nivel de significancia 

            int Opcion;
            double alpha;
            double p, z;

            printf("**************************************\n");
            printf("Selecciona la opcion deseada: \n");
            printf("[1] Calcular Za.\n");
            printf("[2] Calcular Za/2.\n");
            printf("**************************************\n");
            scanf("%d", &Opcion);
            printf("--------------------------------------\n");

            printf("Dame el valor de alpha: ");
            scanf("%lf", &alpha);

            if(Opcion == 1)
            {

                p = 1 - alpha;
                z = Calc_Z(p);

                printf("--------------------------------------\n");
                printf("El valor de Z es: %.4f\n", z);


            }

            else if (Opcion == 2)
            {

                p = 1 - alpha / 2;
                z = Calc_Z(p);

                printf("--------------------------------------\n");
                printf("El valor de Z es: %.4f\n", z);


            }

            else
            {

                printf("--------------------------------------\n");
                printf("Opcion no valida.\n");
                return 0;

            }

            
            break;

            //-----------------------------------------------

            case 12: //Localizar T
                
            // 1. crear funcion que calcule el valor de T con Los grados de libertad y alpha

            break;

            //-----------------------------------------------

            case 13: //Localizar grados de libertad y T
                

            // crear funcion que busque los grados de libertar y alpha dando el valore T

            break;

            //-----------------------------------------------

        }
        
    }
    while (opc > 0);

    printf("Gracias por usar el programa, hasta luego!\n");
    printf("------------------------------------------------------\n");

    return 0;

}

// funciones 

void bubbleSort(int arr[], int n)
{


    int i, j, temp;
    for(i = 0; i < n; i++)
    {
        for(j = 0; j < n-i-1; j++)
        {
            if( arr[j] > arr[j+1])
            {
                //Intercambia las variables
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }


}




float mediana(int arr[], int n)
{
    if(n % 2 != 0)
    {
        return arr[n/2];
    }
    else
    {
        return (arr[n / 2 - 1] + arr[n/2]) / 2.0;
    }
}




float media (int arr[], int n)
{
    float sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += arr[i];
    }
    return sum / n;
}

float moda (int arr[], int n)
{

 int ContadorMax = 0; // Contador de la frecuencia máxima
    int moda = -1; // Valor de la moda
    for (int i = 0; i < n; i++)
    {
        int contador = 0; // Contador para la frecuencia del elemento actual
        for (int j = 0; j < n; j++) 
        {
            if (arr[j] == arr[i]) 
            {
                contador++;
            }
        }
        if (contador > ContadorMax) 
        {
            ContadorMax = contador;
            moda = arr[i];
        }
    }
    return moda;

}

float media_recortada(int arr[], int n, float porcentaje)
{

    bubbleSort(arr, n);
    int recorte = n * porcentaje; // Recortamos el porcentaje de los datos
    float sum = 0;
    for (int i = recorte; i < n - recorte; i++) 
    {
        sum += arr[i];
    }
    return sum / (n - 2 * recorte);

}

float varianza_for1(int arr[], int n, float media, int *contador)
{

    float sum_cuadrados = 0.0;

    for(int i = 0; i < n; i++)
    {

        sum_cuadrados += pow(arr[i] - media, 2);
        (*contador)++;

    }

    return sum_cuadrados / (n -1);

}

float varianza_for2(int arr[], int n, float media, int *contador)
{

    float sum_cuadrados = 0.0;
    float sum = 0.0;

    for(int i = 0; i < n; i++)
    {

        sum_cuadrados += pow(arr[i], 2);
        sum += arr[i];
        (*contador)++;

    }

    return (sum_cuadrados -pow(sum, 2) / n) / (n -1 );

}

double calcular_tiempo(struct timespec start, struct timespec end)
{

    return (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9;
}


double Calc_Z(double Alpha)
{
    // calcula el valor de Za/2 o Za
    double x = 1 - 2 * Alpha;


    // se determina el signo
    double sgn = (x < 0) ? -1.0f : 1.0f;

    // calcula la funcion inversa
    x = (1 - x) * (1 + x);    
    double Log = log(x);
    double Temp1 = 2 / (M_PI * 0.147) + 0.5f * Log; 
    double Temp2 = 1 / (0.147) * Log;
    double resultado = sgn * sqrt(-Temp1 + sqrt(Temp1 * Temp1 - Temp2));

    // se multiplica por sqrt(2) para ajustar la distribucion normal estandar
    return sqrt(2) * resultado;

}

double Calc_T(double Alpha, int NivSig)
{





}