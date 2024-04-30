#include<stdio.h>

int main()
{
 int array[10];
 int i;

    for( i = 0; i < 10;i++)
    {
        printf("elemento [%d] del arrego: ", i+1);
        scanf("%d", &array[i]);
    }

    printf("Elements in array are: ");
    for(i = 0; i < 10; i++)
    {
        printf("%d ", array[i]);
    }
    printf("\n");
    
    return 0;
}