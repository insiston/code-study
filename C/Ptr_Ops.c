#include <stdio.h>

int main()
{
    int urn[5] = {100,200,300,400,500};
    int *ptr1,*ptr2,*ptr3;  // 声明指针

    ptr1 = urn;     // 把一个地址赋给指针
    ptr2 = &urn[2]; // 同上

    printf("pointer value,dereferenced pointer,pointer address: \n");
    printf("ptr1 = %p, *ptr1 = %d, &ptr1 = %p\n",ptr1,*ptr1,&ptr1);     // 取得指针指向的值,并且得到指针的地址

    // 指针加法
    ptr3 = ptr1 + 4;
    printf("\nadding an int to a pointer:\n");
    printf("ptr1 + 4 = %p, *(ptr1 + 3) = %d\n",ptr1 + 4,*(ptr1 + 3));

    // 递增指针
    ptr1++;
    printf("\nvalues after ptr1++\n");
    printf("ptr1 = %p, *ptr1 = %d, &ptr1 = %p\n",ptr1,*ptr1,&ptr1);

    // 递减指针
    ptr2--;
    printf("\nvalues after --ptr2\n");
    printf("ptr2 = %p, *ptr2 = %d, &ptr1 = %p\n",ptr2,*ptr2,&ptr2);

    // 恢复为初始值
    --ptr1;
    ++ptr2;
    printf("\nPointers reset to original values: \n");
    printf("ptr1 = %p, ptr2 = %p\n",ptr1,ptr2);

    // 一个指针减去另一个指针
    printf("\nsubtracting one pointer from another: \n");
    printf("ptr2 = %p, ptr1 = %p, ptr2 - ptr1 = %d\n",ptr2,ptr1,ptr2 - ptr1);

    // 一个指针减去一个整数
    printf("\nsubtracting an int from a pointer: \n");
    printf("ptr3 = %p, ptr3 - 2 = %p\n",ptr3,ptr3 - 2);

    return 0;
}