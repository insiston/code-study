#include <stdio.h>

int getIndex(int arr[], int value)
{
	int i;
	int index;
	for (i = 0;i<5;i++)
	{
		/* �����ѯ���� */
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
	int index = getIndex(arr,value);      //������arr��valueֵ���뺯����
	if (index != -1)
	{
		printf("��Ҫ���ҵ� %d �������д��ڣ��±�Ϊ��%d\n\n", value, index);
	}
	else
	{
		printf("��Ҫ���ҵ� %d �������в����ڡ�\n\n", value);
	}
	printf("�������������...");
	getchar();
	return 0;
}