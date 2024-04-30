#include <stdio.h>
#include <stdlib.h>

int main()
{

    int n;

    printf("Enter size of array\n");
    scanf("%d", &n);

    int *A = (int*)malloc(n*sizeof(int));
    for(int i = 0; i < n; i++)
        A[i] = i + 1;

    printf("---------\n");
    for(int i = 0; i < n; i++)
    {

        printf("%d\n", A[i]);

    }
    printf("---------\n");

    free(A);
    A = NULL;

    return 0;

}