//librerias
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//structs
struct books 
{
    char title[50];
    char author[50];
    char subject[50];
    int book_id;
};



//codigo main
int main()
{

    struct books book1;
    struct books book2;

    strcpy( book1.title, "C programing");
    strcpy( book1.author, "Nuha Ali");
    strcpy( book1.subject, "C programing Tutorial");
    book1.book_id = 6495407;

    strcpy( book2.title, "Telecom Billing");
    strcpy( book2.author, "Zara Ali");
    strcpy( book2.subject, "Telecon Billing Tutorial");
    book2.book_id = 6495700;

    printf("book 1 title: %s\n",book1.title);
    printf("book 1 author: %s\n",book1.author);
    printf("book 1 subject: %s\n",book1.subject);
    printf("book 1 book id: %d\n",book1.book_id);



    printf("book 2 title: %s\n",book2.title);
    printf("book 2 author: %s\n",book2.author);
    printf("book 2 subject: %s\n",book2.subject);
    printf("book 2 book id: %d\n",book2.book_id);


}