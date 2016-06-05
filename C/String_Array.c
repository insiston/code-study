/* 字符串与数组
 * 字符串就是由多个字符组合而成的一段话
 */

#include <stdio.h>

void say(char string[],char _string[])
{
	/* 打印字符串 */
	printf("%s\n", string);  
	printf("%s\n", _string);
}

int main()
{
	/* 定义第一种格式字符串数组 */
	char string[] = "字符串数组"; 

	/* 定义第二种格式字符串数组
	 * 最后一个元素必须是'\0','\0'表示字符串的结束标志
	 * 下面这种定义不能写中文
	*/
	char _string[] = { 'I',' ','L','o','v','e',' ','C','\0' };
	say(string, _string);    //调用say函数输出字符串

	printf("\n按任意结束程序...");
	getchar();
	return 0;
}
