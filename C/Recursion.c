#include <stdio.h>

/* 
 * 递归练习
 * 要求用户输入一个大于0的数,如何不大于0一值提示,知道大于0为止
 */

void scanNumber(); /* ISO/ANSI C函数原型 */

int main(int argc, char *argv[]) {

	scanNumber();
	return 0;
}


void scanNumber() {

	// 接收值
	printf("请输入一个大于0的数字: ");
	int number = -1;
	scanf("%d", &number);

	/* 判断
	 * 递归要有明确的结束条件,防止死循环
	 */
	if (number <= 0) {
		scanNumber();
	}
	else {
		printf("m=%d\n", number);
	}
}