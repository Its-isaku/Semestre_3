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

// Funcion para dibujar el histograma
void dibujarHistograma(int* datos, int tamano) {
    int anchoVentana = 1200; // Ancho de la ventana grafica
    int altoVentana = 600;  // Alto de la ventana grafica
    int anchoBarra = 15;    // Ancho de cada barra
    int espacio = 10;       // Espacio entre barras

    // Calcular el ancho necesario de la ventana
    int anchoNecesario = tamano * (anchoBarra + espacio) + 100; // +100 para margenes

    // Ajustar el ancho de la ventana si es necesario
    if (anchoNecesario > anchoVentana) {
        anchoVentana = anchoNecesario;
    }

    int gd = DETECT, gm;
    initwindow(anchoVentana, altoVentana, "Histograma");

    int maxValor = datos[0];
    for (int i = 1; i < tamano; i++) {
        if (datos[i] > maxValor) {
            maxValor = datos[i];
        }
    }

    int escala = (altoVentana - 100) / maxValor; // Escala para la altura del histograma
    int xInicial = 50;
    int yBase = altoVentana - 50;

    for (int i = 0; i < tamano; i++) {
        int altura = datos[i] * escala;
        int x1 = xInicial + i * (anchoBarra + espacio);
        int y1 = yBase - altura;
        int x2 = x1 + anchoBarra;
        int y2 = yBase;

        rectangle(x1, y1, x2, y2);
        floodfill((x1 + x2) / 2, (y1 + y2) / 2, WHITE);

        // Dibujar etiquetas
        char etiqueta[10];
        sprintf(etiqueta, "%d", datos[i]);
        outtextxy(x1 + 5, y1 - 20, etiqueta);
    }

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

    dibujarHistograma(datos, tamano);

    free(datos);
    return 0;
}
