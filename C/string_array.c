#include <stdio.h>

/* �ַ���������
 * �ַ��������ɶ���ַ���϶��ɵ�һ�λ� 
 */

void say(char string[],char _string[])
{
	/* ��ӡ�ַ��� */
	printf("%s\n", string);  
	printf("%s\n", _string);
}

int main()
{
	/* �����һ�ָ�ʽ�ַ������� */
	char string[] = "�ַ�������"; 

	/* ����ڶ��ָ�ʽ�ַ�������
	 * ���һ��Ԫ�ر�����'\0','\0'��ʾ�ַ����Ľ�����־
	 * �������ֶ��岻��д����
	*/
	char _string[] = { 'I',' ','L','o','v','e',' ','C','\0' };
	say(string, _string);    //����say��������ַ���

	printf("\n�������������...");
	getchar();
	return 0;
}