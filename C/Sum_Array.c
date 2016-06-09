#include <stdio.h>
#define SIZE 10

int sump(int *start,int *end);

int main()
{
    int marbles[SIZE] = {20,10,5,39,4,16,19,26,31,20};
    long answer;
    /*
     * 指向marbles首元素地址
     * 由于索引是从0开始,因此marbles + SIZE 指向数组结尾处之后的下一个元素
     * 如果要让marbles + SIZE指向最后一个元素,则 marbles + SIZE - 1
     */
    answer = sump(marbles,marbles + SIZE);
    printf("The total number of marbles is %ld.\n",answer);
    return 0;
}

int sump(int *start,int *end)
{
    int total = 0;
    while (start < end)
    {
        total += *start;    /* 把值累加到total上 */
        start++;            /* 把指针向前推进到下一个元素 */
    }
    return total;
}