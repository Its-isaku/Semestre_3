#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    uint32_t width;
    uint32_t height;
} Dimensiones_PNG;

int main() {
    char fileName[256];
    printf("Ingrese el nombre del archivo binario: ");
    scanf("%255s", fileName);

    FILE *file = fopen(fileName, "rb");
    if (!file) {
        perror("Error al abrir el archivo");
        return 1;
    }

    const unsigned char FirmaPNG[8] = {0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A};
    unsigned char buffer[8];
    int encontrado = 0;

    // Leer el archivo completo en busca del encabezado PNG
    while (fread(buffer, 1, 8, file) == 8) {
        if (memcmp(buffer, FirmaPNG, 8) == 0) {
            printf("Archivo PNG encontrado.\n");
            encontrado = 1;
            break;
        }
        // Retrocede 7 bytes para no saltarse posibles coincidencias
        fseek(file, -7, SEEK_CUR);
    }

    if (!encontrado) {
        printf("No se encontró un archivo PNG en el archivo binario.\n");
        fclose(file);
        return 1;
    }

    // Saltar a la posición del chunk IHDR después de la firma PNG
    fseek(file, 12, SEEK_CUR); // Saltar 12 bytes desde la firma hasta el comienzo del chunk IHDR

    Dimensiones_PNG dimensiones;
    if (fread(&dimensiones, sizeof(Dimensiones_PNG), 1, file) != 1) {
        fprintf(stderr, "Error al leer las dimensiones del PNG.\n");
        fclose(file);
        return 1;
    }

    // Convertir de big-endian a host byte order
    dimensiones.width = __builtin_bswap32(dimensiones.width);
    dimensiones.height = __builtin_bswap32(dimensiones.height);

    printf("Ancho: %u px\n", dimensiones.width);
    printf("Altura: %u px\n", dimensiones.height);
    fclose(file);
    return 0;
}
