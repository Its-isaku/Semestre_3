//Declaracion de librerias
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

// defino las columnas y las filas para calcular T
#define FILAS 30
#define COLUMNAS 7

//defino constante para histograma
#define Datos_Maximos 100

//defino estructuras
typedef struct {
    int gdl;
    double values[COLUMNAS];
} Valores;



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
int leer_tabla(const char *archivo, Valores *tabla);
double buscar_valor_t(Valores *tabla, int num_filas, int gdl, double alpha);
void buscar_por_t(Valores *tabla2, int num_filas2, double valor_t2);


//codigo main
int main()
{

    int opc;

    do
    {   
        
        struct timespec start, end;
        double tiempo_formula1, tiempo_formula2;

        printf("******************************************************\n");
        printf("Bienvendo alproyecto final de estadistica!\n");
        printf("******************************************************\n");
        printf("\n");
        printf("----------rutinas para graficos----------\n");
        printf("[1]Tallos y hojas........................\n[2]Grafa de puntos.......................\n[3]Histograma............................\n");
        printf("\n");
        printf("----------rutinas para calcular----------\n");
        printf("[4]Moda..................................\n[5]Media.................................\n[6]Media recortada.......................\n[7]Mediana...............................\n");
        printf("[8]Varianza y desviacion estandar........\n");
        printf("\n");
        printf("--------rutinas para Tablas(Z y T)-------\n");
        printf("[9]Calcular valores alha(tabla Z).......\n[10]Encontrar Z con alpha................\n[11]Localizar T..........................\n[12]Localizar grados de libertad y T.....\n[13]Diagrama de dispercion y regresion lineal.....\n");
        printf("\n");
        printf("--------------Otras opciones-------------\n");
        printf("[0]salir....................\n");
        printf("\n");
        printf("******************************************************\n");
        printf("Que deceas hacer? ");
        scanf("%d", &opc);
        printf("******************************************************\n");

        int n;
        int *arr;
        float porcentaje;

        switch (opc)
        {
            //----------------------------------------------------------------------------------------------------------------------------------------------------------------------
            case 1: //Tallos y hojas - Despues
                
            break;

            //----------------------------------------------------------------------------------------------------------------------------------------------------------------------

            case 2: //Grafica de puntos - Despues
                
            break;

            //----------------------------------------------------------------------------------------------------------------------------------------------------------------------

            case 3: //Histograma -Despues
                
            break;

            //----------------------------------------------------------------------------------------------------------------------------------------------------------------------

            case 4: // Moda
            case 5: // Media
            case 7: // Mediana

            int opc2;
            printf("Quieres leer los datos de un archivo o propocionarlos tu?\n******************************************************\n[1] De un archivo\n[2] Dar los datos\n******************************************************\n");
            scanf("%d", &opc2);
            printf("******************************************************\n");

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
                case 4: // Moda
                    printf("La moda del arreglo es : %.2f\n", moda(arr, n));
                    break;

                case 5: // Media
                    printf("La media del arreglo es : %.2f\n", media(arr, n));
                    break;

                case 7: // Mediana
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
                case 4: // Moda
                    printf("La moda del arreglo es : %.2f\n", moda(arr, n));
                    break;

                case 5: // Media
                    printf("La media del arreglo es : %.2f\n", media(arr, n));
                    break;

                case 7: // Mediana
                    printf("La mediana del arreglo es : %.2f\n", mediana(arr, n));
                    break;
                }

                // Liberar la memoria asignada
                free(arr);
                break;

            }

            //-----------------------------------------------

            case 6: // Media recortada

            int opc3;
            printf("Quieres leer los datos de un archivo o propocionarlos tu?\n******************************************************\n[1] De un archivo\n[2] Dar los datos\n******************************************************\n");
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

            case 8: //Varianza y Desviacion estandar
                
            int opc4;
            printf("Quieres leer los datos de un archivo o propocionarlos tu?\n******************************************************\n[1] De un archivo\n[2] Dar los datos\n******************************************************\n");
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

            //----------------------------------------------------------------------------------------------------------------------------------------------------------------------

            case 9: //Calcular valores alha(tabla Z y graficar area bajo la curva) - Despues


                
            break;

            //----------------------------------------------------------------------------------------------------------------------------------------------------------------------
            case 10: //Encontrar Z con alpha y el nivel de significancia 

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

            case 11: //Localizar T dando alpha y grados de libertad
                
            Valores tabla[FILAS];
            int num_filas = leer_tabla("Tabla_T.txt", tabla);
        
            if (num_filas == -1) 
            {
                return 1;
            }
        
            int gdl;
            double alphat;
        
            // Pedir al usuario que ingrese los grados de libertad y el nivel de significancia
            printf("Ingrese los grados de libertad (gdl): ");
            scanf("%d", &gdl);
            printf("Ingrese el nivel de significancia (alpha): ");
            scanf("%lf", &alphat);
        
            // Buscar el valor T
            double t_valor = buscar_valor_t(tabla, num_filas, gdl, alphat);
            if (t_valor != -1.0) 
            {
            printf("El valor T con %d grados de libertad y %.5f como nivel de significancia es: %.3f\n", gdl, alphat, t_valor);
            }

            break;

            //-----------------------------------------------

            case 12: //Localizar grados de libertad y alpha con T
                

            Valores tabla2[FILAS];
            int num_filas2 = leer_tabla("Tabla_T.txt", tabla2);

            if (num_filas2 == -1) {
                return 1;
            }

            double valor_t2;

            // Pedir al usuario que ingrese el valor T
            printf("Ingrese el valor T: ");
            scanf("%lf", &valor_t2);

            // Buscar el valor T en la tabla
            buscar_por_t(tabla2, num_filas2, valor_t2);

            break;

            //----------------------------------------------------------------------------------------------------------------------------------------------------------------------


            case 13: //Diagrama de dispercion y regression lineal

                // Define la ruta al archivo .exe que deseas ejecutar
                const char *path_to_exe = "C:\\Users\\RogSt\\Desktop\\Coding\\Proyecto_Est\\Programas-Graficos\\regresion-lineal.exe";

                // Usa la función system para ejecutar el archivo .exe
                int result = system(path_to_exe);

                // Verifica si la ejecución fue exitosa
                if (result == -1) {
                    printf("Error al intentar ejecutar el archivo .exe\n");
                } else {
                    printf("El archivo .exe se ejecutó correctamente\n");
                }

            break;

            //----------------------------------------------------------------------------------------------------------------------------------------------------------------------

        }
        
    }
    while (opc > 0);

    printf("Gracias por usar el programa, hasta luego!\n");
    printf("******************************************************\n");

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

int leer_tabla(const char *archivo, Valores *tabla) 
{
    FILE *file = fopen(archivo, "r");
    if (file == NULL) 
    {
        printf("No se pudo abrir el archivo %s\n", archivo);
        return 0;
    }

    char header[256]; // Para saltar la primera línea del archivo
    fgets(header, sizeof(header), file);

    int index = 0;
    while (index < FILAS && fscanf(file, "%d %lf %lf %lf %lf %lf %lf %lf",
                            &tabla[index].gdl,
                            &tabla[index].values[0],
                            &tabla[index].values[1],
                            &tabla[index].values[2],
                            &tabla[index].values[3],
                            &tabla[index].values[4],
                            &tabla[index].values[5],
                            &tabla[index].values[6]) == 8) 
                            {
                                index++;
                            }   

    fclose(file);
    return index; // Número de filas leídas
}

// Función para buscar el valor T dado df y alpha
double buscar_valor_t(Valores *tabla, int num_filas, int gdl, double alphat) 
{
    int col = -1;

    // Selecciona la columna correspondiente basada en el nivel de significancia
    if (alphat == 0.10) col = 0;
    else if (alphat == 0.05) col = 1;
    else if (alphat == 0.025) col = 2;
    else if (alphat == 0.01) col = 3;
    else if (alphat == 0.00833) col = 4;
    else if (alphat == 0.00625) col = 5;
    else if (alphat == 0.005) col = 6;
    else {
        printf("Nivel de significancia no valido.\n");
        return -1.0;
    }

    // Busca el valor T en la fila correspondiente a los grados de libertad (gdl)
    for (int i = 0; i < num_filas; i++) 
    {
        if (tabla[i].gdl == gdl) 
        {
            return tabla[i].values[col];
        }
    }

    printf("Grados de libertad no encontrados.\n");
    return -1.0;
}

// Encuentra el índice de columna basado en el valor más cercano
int encontrar_columna(Valores *fila, int num_cols, double valor_t) 
{
    int col = -1;
    double diferencia_minima = 1e10;

    for (int i = 0; i < num_cols; i++) 
    {
        double diferencia = fabs(fila->values[i] - valor_t);
        if (diferencia < diferencia_minima) 
        {
            diferencia_minima = diferencia;
            col = i;
        }
    }

    return col;
}

// Devuelve la descripción textual del nivel de significancia
const char *nivel_significancia(int col) 
{
    if (col == 0)
    {
        return "0.10";
    }
    else if (col == 1)
    {
        return "0.05";
    }
    else if (col == 2)
    {
        return "0.025";
    }
    else if (col == 3)
    {
        return "0.01";
    }
    else if (col == 4)
    {
        return "0.00833";
    }
    else if (col == 5)
    {
        return "0.00625";
    }
    else if (col == 6)
    {
        return "0.005";
    }
    else
    {
        return "desconocido";
    }
}

// Busca los grados de libertad y nivel de significancia dado un valor T
void buscar_por_t(Valores *tabla2, int num_filas2, double valor_t2) {
    int gdl_encontrado = -1;
    int col_encontrada = -1;
    double diferencia_minima = 1e10;

    // Buscar por cada fila para encontrar el valor T más cercano
    for (int i = 0; i < num_filas2; i++) {
        int col = encontrar_columna(&tabla2[i], COLUMNAS, valor_t2);
        double diferencia = fabs(tabla2[i].values[col] - valor_t2);

        if (diferencia < diferencia_minima) {
            diferencia_minima = diferencia;
            gdl_encontrado = tabla2[i].gdl;
            col_encontrada = col;
        }
    }

    if (gdl_encontrado != -1 && col_encontrada != -1) {
        printf("Grados de libertad (gdl) mas cercanos: %d\n", gdl_encontrado);
        printf("Nivel de significancia mas cercano: %s\n", nivel_significancia(col_encontrada));
    } else {
        printf("No se encontraron resultados para el valor T proporcionado.\n");
    }
}