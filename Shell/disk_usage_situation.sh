#!/bin/bash
#Author: vforbox
#Script_file : disk_usage_situation.sh

if [ ! -e disk_usage_situation.log ];
        then
        printf "%-10s|%-15s|%-28s|%-8s|%-6s|%-6s|%-6s|%s\n" "Date" "IP address" "Device" "Capacity" "Used" "Free" "Percent" "Status" > disk_usage_situation.log
fi

read -p "Please enter the IP/host: " IP_LIST
read -p "Please enter Port[Default 22]: " Port
read -p "please enter account name: " user
(
for ip in $IP_LIST;
do
        ssh $user@$ip -p $Port 'df -H' | grep ^/dev/ > /tmp/log.df

        while read line;
        do
                cur_date=$(date +"%Y-%m-%d")
                printf "%-10s|%-15s|" $cur_date $ip
                echo $line | awk '{printf ("%-28s|%-8s|%-6s|%-6s|%-7s",$1,$2,$3,$4,$5);}'

        pusg=$(echo $line | egrep -o "[0-9]+%")
        pusg=${pusg/\%/};
        if [ $pusg -lt 80 ];
                then
                echo "|Safe"
        else
                echo "|Alert"
        fi

        done< /tmp/log.df
done

        ) >> disk_usage_situation.log
rm -rf /tmp/log.df
