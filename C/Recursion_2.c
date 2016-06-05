/*
 * 有5个人坐在一起,问第5个人多少岁,他说比第4个人大2岁
 * 问第4个人岁数,他说比第3个人大2岁
 * 问第3个人,又说比第2人大两岁
 * 问第2个人,说比第1个人大两岁
 * 最后 问第1个人,他说是10岁
 * 请问第5个人多大？
 */

#include <stdio.h>

int getAge(numPeople)
{
	// 定义返回都年龄
	int age;
	// 如果是第一个人的时候,年龄为固定的10岁
	if (numPeople == 1)
		age = 10;
	else
		// 否则递归查询,计算一次人数-1并且+上大的2岁
		age = getAge(numPeople - 1) + 2;
	return age;
}

int main()
{
	// 定义第5个人的年龄,并调用getAge函数获取给其赋值
	int fifthAge = getAge(5);
	printf("第5个人的年龄是 %d 岁",fifthAge);
	printf("\n\n按任意结束程序...");
	getchar();
	return 0;
}