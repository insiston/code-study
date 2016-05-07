#!/bin/bash

# nginx日志目录
nginx_log_dir="/usr/local/nginx/logs/"

# 根据状态码进行请求次数
check_http_status(){
	Http_code=(`cat ${nginx_log_dir}access.log | grep -ioE "HTTP\/1\.[0-9]\"[[:blank:]][0-9]{3}"|awk -F"[ ]+" '{
	if($2>=100 && $2<200)
		{i++}
	else if($2>=200 && $2<300)
		{j++}
	else if($2>=300 && $2<400)
		{k++}
	else if($2>=400 && $2<500)
		{n++}
	else if($2>=500)
		{p++}
	}END{
		print i?i:0,j?j:0,k?k:0,n?n:0,p?n:0,i+j+k+n+p
	}'`)
	
	echo -e "\E[35mHttp 状态码[100+]: \E[0m" ${Http_code[0]}
	echo -e "\E[35mHttp 状态码[200+]: \E[0m" ${Http_code[1]}
	echo -e "\E[35mHttp 状态码[300+]: \E[0m" ${Http_code[2]}
	echo -e "\E[35mHttp 状态码[400+]: \E[0m" ${Http_code[3]}
	echo -e "\E[35mHttp 状态码[500+]: \E[0m" ${Http_code[4]}
	echo -e "\E[35mHttp 状态码总共  : \E[0m" ${Http_code[5]}
}

# 查看所有状态码
detailed_http_code(){
	cat ${nginx_log_dir}access.log | cut -d '"' -f3 | cut -d ' ' -f2 | sort | uniq -c | sort -r | awk '{print "Http 状态码["$2"]: ",$1}'
}

# 用户自定义查询Http状态码请求次数
check_http_code(){
	Http_Code=(`cat ${nginx_log_dir}access.log | grep -ioE "HTTP\/1\.[0-9]\"[[:blank:]][0-9]{3}"|awk -F'[ ]+' '{
	if ($2!="")
		{code[$2]++}
	else
		{exit}
	}END{
		print code['$1']?code['$1']:0
	}'`)
	echo -e "\E[35mHttp 状态码[$1]: \E[0m" ${Http_Code[0]}
	awk '($9 ~ /'$1'/)' ${nginx_log_dir}access.log | awk '{print $7}' | sort | uniq -c | sort -r
}

# 函数调用
check_http_status

echo -e "\E[31m---------------- 分割线 ----------------\E[0m"
read -p "是否需要查看详细的HTTP 状态码[Y|N]: " inquiry
if [ ${inquiry} == 'Y' -o ${inquiry} == 'y' ];then
	detailed_http_code
	echo -e "\E[31m---------------- 分割线 ----------------\E[0m"
	read -p "输入需要查询的状态码: " number
	check_http_code $number

elif [ ${inquiry} == 'N' -o ${inquiry} == 'n' ];then
	
	echo -e "\E[31m---------------- 分割线 ----------------\E[0m"
	read -p "输入需要查询的状态码: " number
	check_http_code $number
else
	echo -e "\e[32m输入错误...! 退出程序.\e[0m"
	exit
fi
