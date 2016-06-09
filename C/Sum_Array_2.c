#include <stdio.h>
#define SIZE 10

/*  如果不能使用%zd,就使用%u或者%lu */
int sum(int ar[],int n);

int main()
{
    int marbles[SIZE]  = {20,10,5,39,4,16,19,26,31,20};
    long answer;
    answer = sum(marbles,SIZE);
    printf("The total number of marbles is %ld.\n",answer);
    printf("The size of marbles is %lu bytes.\n", sizeof marbles);

    return 0;
}

int sum(int ar[],int n)
{
    int i;
    int total = 0;
    for (i = 0;i < n;i++)
        total += ar[i];
    printf("The size of ar is %lu bytes.\n", sizeof ar);   // ar只是指向marbles首元素的指针
    return total;
}