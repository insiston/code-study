/* ��һ������Ϊ10��������������,�����˰༶10��ѧ���Ŀ��Գɼ�
 * Ҫ���д5������,�ֱ�ʵ�ּ��㿼�Ե��ܷ�,��߷�,��ͷ�,ƽ���ֺͿ��Գɼ���������
 */

#include <stdio.h>
#define N 10

//��ӡ���� 
void printScore(int score[])
{
	int i;
	printf("\n");
	for (i = 0;i<N;i++)
	{
		printf("%d ", score[i]);
	}
	printf("\n");
}

//���㿼���ܷ� 
int getTotalScore(int score[])
{
	int sum = 0;
	int i;
	for (i = 0;i<N;i++)
	{
		sum += score[i];
	}
	return sum;
}

//����ƽ���� 
int getAvgScore(int score[])
{
	return getTotalScore(score) / N;
}

//������߷� 
int getMax(int score[])
{
	int max = -1;
	int i;
	for (i = 0;i<N;i++)
	{
		if (score[i]>max)
		{
			max = score[i];
		}
	}
	return max;
}

//������ͷ� 
int getMin(int score[])
{
	int min = 100;
	int i;
	for (i = 0;i<N;i++)
	{
		if (score[i]< min)
		{
			min = score[i];
		}
	}
	return min;
}

//������������ 
void sort(int score[])
{
	int i, j;
	for (i = N - 2;i >= 0;i--)
	{
		for (j = 0;j <= i;j++)
		{
			if (score[j]<score[j + 1])
			{
				int temp;
				temp = score[j];
				score[j] = score[j + 1];
				score[j + 1] = temp;
			}
		}
	}
	printScore(score);
}


int main()
{
	int score[N] = { 67,98,75,63,82,79,81,91,66,84 };
	int sum, avg, max, min;
	sum = getTotalScore(score);
	avg = getAvgScore(score);
	max = getMax(score);
	min = getMin(score);
	printf("----------�������---------\n");
	printf("\t�ܷ��ǣ�%d\n", sum);
	printf("\tƽ�����ǣ�%d\n", avg);
	printf("\t��߷��ǣ�%d\n", max);
	printf("\t��ͷ��ǣ�%d\n", min);
	printf("\n----------�ɼ�����---------\n");
	sort(score);
	printf("\n�������������...");
	getchar();
	return 0;
}

