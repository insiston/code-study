/*
 * struct.c - 结构体练习
 * 结构体是用户自定义的可用数据类型,允许存储不同类型的数据项
 *
 * Author: vforbox <vrobox@gmail.com>
 * Create Date: 2016
 */

#include <stdio.h>
#include <string.h>

/*
 * struct 语句定义了一个包含多个成员的新的数据类型
 * 访问结构体成员,使用成员访问运算符 .
 */
struct Books
{
    char title[20];
    char author[50];
    char subject[100];
    int book_id;
};

/*
 * 函数原型定义
 *
 * book_1 - Book1 的属性
 * book_2 - Book2 的属性
 *
 * Return value: Null
 */
void book_1();
void book_2();

int main()
{
    printf("******************** Book1 ********************\n");
    book_1();
    printf("******************** Book2 ********************\n");
    book_2();
    return 0;
}

/* Book1 属性详述 */
void book_1()
{
    struct Books Book1;     /* 声明 Book1 为 Book */

    strcpy(Book1.title,"C Programming");
    strcpy(Book1.author,"vforbox");
    strcat(Book1.subject,"C Programming");
    Book1.book_id = 6495470;

    /* 输出 Book1 信息 */
    printf("Book 1 title : %s\n", Book1.title);
    printf( "Book 1 author : %s\n", Book1.author);
    printf( "Book 1 subject : %s\n", Book1.subject);
    printf( "Book 1 book_id : %d\n", Book1.book_id);
    return;
}

/* Book2 属性详述 */
void book_2()
{
    struct Books Book2;      /* 声明 Book2 为 Book */

    strcpy(Book2.title,"Python Programming");
    strcpy(Book2.author,"vfobox");
    strcpy(Book2.subject,"Python Programming");
    Book2.book_id = 6495471;

    /* 输出 Book2 信息 */
    printf("Book 2 title : %s\n", Book2.title);
    printf( "Book 2 author : %s\n", Book2.author);
    printf( "Book 2 subject : %s\n", Book2.subject);
    printf( "Book 2 book_id : %d\n", Book2.book_id);
    return;
}
