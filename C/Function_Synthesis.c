#include <stdio.h>

/*
 * 1. ÿ���ﵥ�ۼƷ�2.3Ԫ
 * 2. �𲽼�13Ԫ(����3����)
 * 3. ����23��(��)�������賿5��(����)��,ÿ���ﵥ�ۼƷѼ���20%
 * 4. ÿ�γ˳�����1ԪǮ��ȼ�͸���˰
 * 
 * *** *** *** *** *** *** *** *** *** *** *** *** *** 
 * С��ÿ�����°඼Ҫ��,��˾�ͼҵľ���Ϊ12����,�����ϰ�ʱ��Ϊ9��,�����°�ʱ��Ϊ6��
 * ����С��ÿ��򳵵��ܷ���
 * ** *** *** *** *** *** *** *** *** *** *** *** *** 
 */

/* ʱ��;��� */
double getTaxiPrice(int hours, int distance)
{
	double totalPrice = 0.0;	//����򳵷��� 
	double perPrice = 2.3;	//����ÿ���ﵥ�ۼƷ� 
	int startPrice = 13;	//�����𲽼� 

	if (hours<0 || hours>24) {
		printf("����д��ȷ��ʱ��\n");
		return 0;
	}
	else if (!(hours >= 5 && hours<23))	//�жϴ�ʱ���Ƿ�Ҫ���ӷ���
	{
		perPrice *= 1.2;	//��������20%                         
	}
	if (distance >3)		//�жϹ�����
	{
		totalPrice = startPrice + (distance - 3)*perPrice;	//�����Ǯ
	}
	else
	{
		totalPrice = startPrice;
	}
	totalPrice++;	//��һ��Ǯ��ȼ�ͷ�
	return totalPrice;
}

int main()
{
	int moring = 9;	//���������ʱ��
	int afternoon = 18;	//���������ʱ��
	int distance = 12;	//����򳵹�����
	double totalPrice = 0;	//�����ܷ���
	if (getTaxiPrice(moring, distance) != 0)
	{
		totalPrice = getTaxiPrice(moring, distance);	//���ü�����õĺ���
	}
	else if (totalPrice != 0)
	{
		totalPrice += getTaxiPrice(afternoon, distance);	//���ü�����õĺ���
	}
	printf("С��ÿ��򳵵��ܷ����ǣ�%.2f\n", totalPrice);	//���
	getchar();
	return 0;
}
