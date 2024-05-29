#include <stdio.h>
#include <stdlib.h>
#include <graphics.h>

// Funcion para contar los elementos en el archivo
int contarElementosArchivo(const char* nombreArchivo) {
    FILE* archivo = fopen(nombreArchivo, "r");
    if (!archivo) {
        printf("Error al abrir el archivo.\n");
        return 0;
    }
    int contador = 0;
    int valor;
    while (fscanf(archivo, "%d", &valor) != EOF) {
        contador++;
    }
    fclose(archivo);
    return contador;
}

// Funcion para leer los datos desde el archivo
void leerDatosDesdeArchivo(const char* nombreArchivo, int* datos, int tamano) {
    FILE* archivo = fopen(nombreArchivo, "r");
    if (!archivo) {
        printf("Error al abrir el archivo.\n");
        return;
    }
    for (int i = 0; i < tamano; i++) {
        fscanf(archivo, "%d", &datos[i]);
    }
    fclose(archivo);
}

// Funcion para leer los datos manualmente
void leerDatosManual(int* datos, int tamano) {
    printf("Ingrese %d valores:\n", tamano);
    for (int i = 0; i < tamano; i++) {
        printf("Valor %d: ", i + 1);
        scanf("%d", &datos[i]);
    }
}

// Funcion para dibujar el diagrama de puntos
void dibujarDiagramaDePuntos(int* datos, int tamano) {
    int gd = DETECT, gm;
    int anchoVentana = 1500;
    int altoVentana = 600;
    initwindow(anchoVentana, altoVentana, "Diagrama de Puntos");

    // Encontrar el valor maximo para la escala
    int maxValor = datos[0];
    for (int i = 1; i < tamano; i++) {
        if (datos[i] > maxValor) {
            maxValor = datos[i];
        }
    }

    // Dibujar los puntos
    int margen = 50;
    int espacioEntrePuntos = 10;
    int escalaX = (anchoVentana - 2 * margen) / (tamano - 1);
    int escalaY = (altoVentana - 2 * margen) / maxValor;

    setcolor(WHITE);
    setlinestyle(SOLID_LINE, 0, 2);
    settextstyle(DEFAULT_FONT, HORIZ_DIR, 2);

    // Dibujar ejes
    line(margen, altoVentana - margen, anchoVentana - margen, altoVentana - margen); // Eje X


    // Dibujar etiquetas de los ejes
    settextstyle(DEFAULT_FONT, VERT_DIR, 1); // Cambiar el estilo de texto a vertical
    for (int i = 0; i < tamano; i++) {
        char etiquetaX[5];
        sprintf(etiquetaX, "%d", i + 1);
        outtextxy(margen + i * escalaX, altoVentana - margen + 10, etiquetaX);
    }
    settextstyle(DEFAULT_FONT, HORIZ_DIR, 2); // Volver al estilo de texto horizontal

    // Agrupar datos por valores
    int* contador = (int*)calloc(maxValor + 1, sizeof(int));

    // Dibujar los puntos
    setcolor(RED);
    for (int i = 0; i < tamano; i++) {
        int x = margen + (datos[i] - 1) * escalaX;
        int y = altoVentana - margen - (contador[datos[i]] * espacioEntrePuntos);
        fillellipse(x, y, 5, 5);  // Dibujar un punto (circulo peque�o)
        contador[datos[i]]++;
    }

    free(contador);

    getch();
    closegraph();
}

int main() {
    int opcion;
    printf("******************************************************\n");
    printf("[1]De un archivo\n[2] Dar los datos\nQue deseas hacer: ");
    scanf("%d", &opcion);
    printf("******************************************************\n");

    int tamano;
    int* datos;

    if (opcion == 1) {
        const char* nombreArchivo = "C:\\Users\\RogSt\\Desktop\\Coding\\Proyecto_Est\\Programas-Graficos\\prueba.txt";
        tamano = contarElementosArchivo(nombreArchivo);
        datos = (int*)malloc(tamano * sizeof(int));
        leerDatosDesdeArchivo(nombreArchivo, datos, tamano);
    } else if (opcion == 2) {
        printf("Ingrese la cantidad de valores: ");
        scanf("%d", &tamano);
        datos = (int*)malloc(tamano * sizeof(int));
        leerDatosManual(datos, tamano);
    } else {
        printf("Opcion no valida.\n");
        return 1;
    }

    dibujarDiagramaDePuntos(datos, tamano);

    free(datos);
    return 0;
}

