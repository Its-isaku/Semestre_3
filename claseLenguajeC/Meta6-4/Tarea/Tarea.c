#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main()
{

    const char *png_salida = "imagen_extraida.png";

    //Verifico que la imagen se pueda abrir
    FILE *fptr = fopen("MegaMind.bin", "rb");
    if (fptr == NULL)
    {
        // mando error si no se puede abrir
        printf("File cannot be opened");
        exit(0);

    }
    // busco dentro del archivo binario la firma de una imagen png
    unsigned char firma_Png[8] = {137, 80, 78, 71, 13, 10, 26, 10};
    unsigned char buffer[8];
    int encontrada_Png = 0;

    //buscola firma 
    while (fread(buffer, 1, sizeof(buffer), fptr) == sizeof(buffer))
    {

        if (memcmp(firma_Png, buffer, sizeof(buffer)) == 0)
        {
            //la firma png coincide
            encontrada_Png = 1;
            //retrocede para leer la imagen completa
            fseek(fptr, -sizeof(buffer), SEEK_CUR);
            break;

        }

        //retrocede 7 bytes para la siguiente comparacion
        fseek(fptr, -7, SEEK_CUR); 

    }

    if (!encontrada_Png)
    {
        printf("No se encontró una imagen PNG en el archivo.\n");
        fclose(fptr);
        return 0;

    }

    //crear archivo para guardar la imagen
    FILE *imagen = fopen (png_salida, "wb");
    if (imagen == NULL)
    {

        printf("Error al abrir el archivo de salida.\n");
        fclose(fptr);
        return 0;

    }

    //copiar los datos de la imagen PNG al nuevo archivo
    size_t bytes_read;
    while ((bytes_read = fread(buffer, 1, sizeof(buffer), fptr)) > 0)
    {

        fwrite(buffer, 1, bytes_read, imagen);

    }

    fclose(imagen);
    fclose(fptr);

    printf("La imagen PNG ha sido extraida y guardada en %s\n", png_salida);

    return 0;
}