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

// Funcion para dibujar la grafica de tallos y hojas
void dibujarTallosYHojas(int* datos, int tamano) {
    int gd = DETECT, gm;
    initwindow(600, 400, "Grafica de Tallos y Hojas");

    // Ordenar los datos
    for (int i = 0; i < tamano - 1; i++) {
        for (int j = 0; j < tamano - i - 1; j++) {
            if (datos[j] > datos[j + 1]) {
                int temp = datos[j];
                datos[j] = datos[j + 1];
                datos[j + 1] = temp;
            }
        }
    }

    // Variables para la grafica
    int xInicial = 100;
    int yInicial = 50;
    int yOffset = 20;
    int tamanoFuente = 2;

    // Dibujar tallos y hojas
    int talloAnterior = -1;
    for (int i = 0; i < tamano; i++) {
        int tallo = datos[i] / 10;
        int hoja = datos[i] % 10;

        if (tallo != talloAnterior) {
            char buffer[10];
            sprintf(buffer, "%d |", tallo);
            outtextxy(xInicial, yInicial, buffer);
            yInicial += yOffset;
            talloAnterior = tallo;
        }

        char hojaStr[2];
        sprintf(hojaStr, "%d", hoja);
        outtextxy(xInicial + 50 + (i % 10) * 10, yInicial - yOffset, hojaStr);
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

    dibujarTallosYHojas(datos, tamano);

    free(datos);
    return 0;
}
