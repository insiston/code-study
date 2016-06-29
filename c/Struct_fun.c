/*
 * struct.c - 结构作为函数参数
 *
 * Author: vforbox <vrobox@gmail.com>
 * Create Date: 2016 
 */

#include <stdio.h>
#include <string.h>

struct Books
{
    char title[20];
    char author[50];
    char subject[100];
    int book_id;
};

/*
 * printBook -  输出 Book 信息
 * @book: 声明 book,类型为 Book
 */
void printBook( struct Books book );

int main()
{
    struct Books Book1;        /* 声明 Book1，类型为 Book */
    struct Books Book2;        /* 声明 Book2，类型为 Book */

    /* Book1 属性详述 */
    strcpy(Book1.title,"C Programming");
    strcpy(Book1.author,"vforbox");
    strcat(Book1.subject,"C Programming");
    Book1.book_id = 6495470;

    /* Book2 属性详述 */
    strcpy(Book2.title,"Python Programming");
    strcpy(Book2.author,"vfobox");
    strcpy(Book2.subject,"Python Programming");
    Book2.book_id = 6495471;

    printf("******************** Book1 ********************\n");

    /* 输出 Book1 信息 */
    printBook( Book1 );

    printf("******************** Book2 ********************\n");

    /* 输出 Book2 信息 */
    printBook( Book2 );
    return 0;
}

void printBook( struct Books book )
{
    printf( "Book title : %s\n", book.title);
    printf( "Book author : %s\n", book.author);
    printf( "Book subject : %s\n", book.subject);
    printf( "Book book_id : %d\n", book.book_id);
}
