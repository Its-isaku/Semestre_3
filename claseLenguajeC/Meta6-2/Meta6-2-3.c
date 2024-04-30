#include <stdio.h>
#include <stdlib.h>

int main()
{

    int* ptr;
    int n ,i;

    n = 5;
    printf("Enter number of elements: %d\n", n);
    ptr = (int*)calloc(n, sizeof(int));

    if (ptr == NULL)
    {
        printf("Memory not allocated.\n");
        exit(0);
    }

    else 
    {

        printf("Memory succesfully allocated using calloc.\n");

        for(i = 0; i < n; i++)
        {
            ptr[i] = i + 1;
        }

        printf("The elements od the array are: ");
        for(i = 0; i < n; i++)
        {
            printf("%d, ", ptr[i]);
        }

        n = 10;
        printf("\n\nEnter the new size uf the array: %d\n", n);

        ptr = realloc(ptr, n * sizeof(int));

        printf("Memory succesfully re-allocated using realloc.\n");

        for(i = 5; i < n; i++)
        {
            ptr[i] = i + 1;
        }

        printf("The elements od the array are: ");
        for(i = 0; i < n; i++)
        {
            printf("%d, ", ptr[i]);
        }

        free(ptr);
        ptr == NULL;



    }

    return 0;

}