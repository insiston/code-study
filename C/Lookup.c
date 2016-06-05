#include <stdio.h>

int getIndex(int arr[], int value)
{
	int i;
	int index;
	for (i = 0;i<5;i++)
	{
		/* 数组查询功能 */
		if (arr[i] == value)
		{
			index = i;
			break;
		}
		else
		{
			index = -1;
		}
	}
	return index;
}

int main()
{
	int arr[] = { 3,12,9,8,6 };
	int value = 8;
	int index = getIndex(arr,value);      //将数组arr和value值传入函数中
	if (index != -1)
	{
		printf("需要查找的 %d 在数组中存在，下标为：%d\n\n", value, index);
	}
	else
	{
		printf("需要查找的 %d 在数组中不存在。\n\n", value);
	}
	printf("按任意结束程序...");
	getchar();
	return 0;
}