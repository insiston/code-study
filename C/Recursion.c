#include <stdio.h>

/* 
 * �ݹ���ϰ
 * Ҫ���û�����һ������0����,��β�����0һֵ��ʾ,֪������0Ϊֹ
 */

void scanNumber(); /* ISO/ANSI C����ԭ�� */

int main(int argc, char *argv[]) {

	scanNumber();
	return 0;
}


void scanNumber() {

	// ����ֵ
	printf("������һ������0������: ");
	int number = -1;
	scanf("%d", &number);

	/* �ж�
	 * �ݹ�Ҫ����ȷ�Ľ�������,��ֹ��ѭ��
	 */
	if (number <= 0) {
		scanNumber();
	}
	else {
		printf("m=%d\n", number);
	}
}