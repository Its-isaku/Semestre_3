#include <graphics.h>
#include <math.h>
#include <stdio.h>

#define PI 3.14159265358979323846

// Funcion para calcular la funcion de densidad de probabilidad de la distribucion normal estandar
double normal_pdf(double x) {
    return exp(-0.5 * x * x) / sqrt(2 * PI);
}

// Funcion para calcular la integral de la distribucion normal estandar utilizando el metodo del trapecio
double normal_cdf(double z) {
    double sum = 0.0;
    double step = 0.001; // Incremento pequeno para mayor precision
    for (double x = -5.0; x < z; x += step) {
        sum += normal_pdf(x) * step;
    }
    return sum;
}

// Funcion para graficar la curva normal estandar
void plot_normal_distribution(double z) {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    int centerX = getmaxx() / 2;
    int centerY = getmaxy() * 3 / 4; // Mueve el centro mas abajo

    // Dibujar los ejes
    line(0, centerY, getmaxx(), centerY);
    line(centerX, 0, centerX, getmaxy());

    // Dibujar la curva de la distribucion normal
    for (int i = -300; i < 300; i++) { // Ajuste de escala para hacer la grafica menos grande
        double x = i / 30.0; // Ajuste del rango para visualizar mejor
        double y = normal_pdf(x) * 100; // Ajuste de escala para reducir la altura de la grafica
        putpixel(centerX + i, centerY - y, WHITE);
    }

    // Rellenar el area bajo la curva para z
    setfillstyle(SOLID_FILL, BLUE);
    for (int i = -300; i < z * 30; i++) { // Ajuste de escala para hacer la grafica menos grande
        double x = i / 30.0;
        double y = normal_pdf(x) * 100; // Ajuste de escala para reducir la altura de la grafica
        line(centerX + i, centerY, centerX + i, centerY - y);
    }

    getch();
    closegraph();
}

int main() {
    double z;
    printf("Ingrese el valor de z: ");
    scanf("%lf", &z);
    plot_normal_distribution(z);
    return 0;
}
