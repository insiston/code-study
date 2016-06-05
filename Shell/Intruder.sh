#!/bin/bash

Server_login_log=/var/log/secure

if [[ -n $1 ]];
	then
	Server_login_log=$1
	echo Using Log file: $Server_login_log
fi

LOG=/tmp/secure.log
grep -v "livalid" $Server_login_log > $LOG
users=$(grep "Failed password" $LOG | awk '{print $(NF-5) }' | sort | uniq)
printf "%-5s\t|%-10s\t|%-10s|%-13s\t|%-20s\t|%-s\n" "Sr"

ucount=0;
ip_list="$(egrep -o "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" $LOG | sort | uniq)"

for ip in $ip_list;
do
	grep $ip $LOG > /tmp/ip.log

for user in $users;
do
	grep $user /tmp/ip.log> /tmp/user.log
	cut -c-16 /tmp/user.log > log.time
	tstart=$(head -1 log.time);
	start=$(date -d "$tstart" "+%s");
	tend=$(tail -1 log.time);
	end=$(date -d "$tend" "+%s")

	limit=$(( $end - $start ))
	if [ $limit -gt 120 ];
	then
		let ucount++;

	IP=$(egrep -o "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" /tmp/user.log | head -1);
	TIME_RANGE="$tstart---> $tend";
	Attempts=$(cat /tmp/user.log|wc -l);
	HOST=$(echo $IP| awk '{print $NF}' );
	printf "%-5s\t|%-10s\t|%-10s|%-13s\t|%-20s\t|%-s\n" "$ucount" "$user" "$Attempts" "$IP" "$HOST" "$TIME_RANGE";
	 fi
  done
done

rm -rf log.time 

