#include <stdio.h>

int data[2] = {100,200};
int moredata[2] = {300,400};

int main()
{
    int *p1,*p2,*p3;
    p1 = p2 = data;
    p3 = moredata;
    printf(" *p1 = %d, *p2 = %d, *p3 = %d\n",*p1,*p2,*p3);
    printf(" *p1++ = %d, *p2++ = %d, (*p3)++ = %d\n",*p1++,*p2++,(*p3)++);
    /*
     * p1 和 p2 指针,只是指向了下一个数组的元素
     * p3 指针改变了数组元素的值
     */
    printf(" *p1 = %d, *p2 = %d, *p3 = %d\n",*p1,*p2,*p3);
    return 0;
}