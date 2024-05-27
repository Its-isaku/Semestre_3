#include <stdio.h>
#include <stdlib.h>
#include <graphics.h>

#define MAX_PUNTOS 100

void leer_datos(const char *nombre_archivo, int datos_x[], int datos_y[], int *n) {
    FILE *archivo = fopen(nombre_archivo, "r");
    if (archivo == NULL) {
        printf("Error al abrir el archivo.\n");
        exit(1);
    }

    // Leer los datos x
    char header_x;
    fscanf(archivo, " %c", &header_x);
    if (header_x != 'x') {
        printf("Formato del archivo incorrecto. Falta el encabezado 'x'.\n");
        fclose(archivo);
        exit(1);
    }

    int n_x = 0;
    while (n_x < MAX_PUNTOS && fscanf(archivo, "%d", &datos_x[n_x]) == 1) {
        n_x++;
    }

    // Leer los datos y
    char header_y;
    fscanf(archivo, " %c", &header_y);
    if (header_y != 'y') {
        printf("Formato del archivo incorrecto. Falta el encabezado 'y'.\n");
        fclose(archivo);
        exit(1);
    }

    int n_y = 0;
    while (n_y < MAX_PUNTOS && fscanf(archivo, "%d", &datos_y[n_y]) == 1) {
        n_y++;
    }

    fclose(archivo);

    if (n_x != n_y) {
        printf("Cantidad de puntos x y y no coincide.\n");
        exit(1);
    }

    *n = n_x;
}

void ingresar_datos(int datos_x[], int datos_y[], int *n) {
    printf("Ingrese la cantidad de puntos: ");
    scanf("%d", n);
    if (*n > MAX_PUNTOS) {
        printf("Cantidad máxima de puntos excedida.\n");
        exit(1);
    }
    printf("Ingrese los valores de x e y:\n");
    for (int i = 0; i < *n; i++) {
        printf("x[%d]: ", i);
        scanf("%d", &datos_x[i]);
        printf("y[%d]: ", i);
        scanf("%d", &datos_y[i]);
    }
}

void dibujar_grafica_dispersion(int datos_x[], int datos_y[], int n) {
    setcolor(WHITE);
    for (int i = 0; i < n; i++) {
        setfillstyle(SOLID_FILL, BLUE);
        fillellipse(50 + datos_x[i] * 30, 450 - datos_y[i] * 2, 3, 3);
    }
}

void regresion_lineal(int datos_x[], int datos_y[], int n, double *m, double *b) {
    double suma_x = 0, suma_y = 0, suma_xy = 0, suma_xx = 0;
    for (int i = 0; i < n; i++) {
        suma_x += datos_x[i];
        suma_y += datos_y[i];
        suma_xy += datos_x[i] * datos_y[i];
        suma_xx += datos_x[i] * datos_x[i];
    }

    *m = (n * suma_xy - suma_x * suma_y) / (n * suma_xx - suma_x * suma_x);
    *b = (suma_y - *m * suma_x) / n;
}

void dibujar_linea(double m, double b, int x_max) {
    setcolor(RED);
    setlinestyle(SOLID_LINE, 0, THICK_WIDTH);
    int x1 = 0, y1 = 450 - b * 2;
    int x2 = x_max, y2 = 450 - (m * x2 + b) * 2;
    line(50 + x1 * 30, y1, 50 + x2 * 30, y2);
}

int main() {
    int datos_x[MAX_PUNTOS], datos_y[MAX_PUNTOS];
    int n = 0;
    char eleccion;

    printf("******************************************************\n");
    printf("[1] De un archivo\n[2] Dar los datos\nQue deseas hacer? ");
    scanf(" %c", &eleccion);
    printf("******************************************************\n");

    if (eleccion == '1') {
        leer_datos("C:\\Users\\RogSt\\Desktop\\Coding\\Proyecto_Est\\Programas-Graficos\\prueba2.txt", datos_x, datos_y, &n);
    } else {
        ingresar_datos(datos_x, datos_y, &n);
    }

    // Inicializar gráficos
    int gd = DETECT, gm;
    initgraph(&gd, &gm, NULL);

    // Dibujar la gráfica de dispersión
    dibujar_grafica_dispersion(datos_x, datos_y, n);

    // Realizar la regresión lineal y dibujar la línea de ajuste
    double m, b;
    regresion_lineal(datos_x, datos_y, n, &m, &b);
    dibujar_linea(m, b, datos_x[n-1]);

    printf("Regresion lineal: y = %lf * x + %lf\n", m, b);

    // Pausa para mantener la ventana abierta
    getch();
    closegraph();

    return 0;
}

