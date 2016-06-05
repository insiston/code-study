#include <stdio.h>

/*
 * 1. 每公里单价计费2.3元
 * 2. 起步价13元(包含3公里)
 * 3. 晚上23点(含)至次日凌晨5点(不含)打车,每公里单价计费加收20%
 * 4. 每次乘车加收1元钱的燃油附加税
 * 
 * *** *** *** *** *** *** *** *** *** *** *** *** *** 
 * 小明每天上下班都要打车,公司和家的距离为12公里,上午上班时间为9点,下午下班时间为6点
 * 计算小明每天打车的总费用
 * ** *** *** *** *** *** *** *** *** *** *** *** *** 
 */

/* 时间和距离 */
double getTaxiPrice(int hours, int distance)
{
	double totalPrice = 0.0;	//定义打车费用 
	double perPrice = 2.3;	//定义每公里单价计费 
	int startPrice = 13;	//定义起步价 

	if (hours<0 || hours>24) {
		printf("请填写正确的时间\n");
		return 0;
	}
	else if (!(hours >= 5 && hours<23))	//判断打车时间是否要增加费用
	{
		perPrice *= 1.2;	//费用增加20%                         
	}
	if (distance >3)		//判断公里数
	{
		totalPrice = startPrice + (distance - 3)*perPrice;	//计算价钱
	}
	else
	{
		totalPrice = startPrice;
	}
	totalPrice++;	//加一块钱的燃油费
	return totalPrice;
}

int main()
{
	int moring = 9;	//定义上午打车时间
	int afternoon = 18;	//定义下午打车时间
	int distance = 12;	//定义打车公里数
	double totalPrice = 0;	//定义总费用
	if (getTaxiPrice(moring, distance) != 0)
	{
		totalPrice = getTaxiPrice(moring, distance);	//调用计算费用的函数
	}
	else if (totalPrice != 0)
	{
		totalPrice += getTaxiPrice(afternoon, distance);	//调用计算费用的函数
	}
	printf("小明每天打车的总费用是：%.2f\n", totalPrice);	//输出
	getchar();
	return 0;
}
