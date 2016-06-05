#!/bin/bash
#Author: vforbox
#Script_file : img_downloader.sh

if [  $# -ne 3 ];
        then
        echo "Usage: $0 URL -d Directory"
        exit -1
fi
while [ -n "$1" ]
do
        case $1 in
                -d ) shift; directory=$1; shift;;
                 * ) url=${url:-$1};shift;;
        esac
done

mkdir -p $directory
baseurl=$(echo $url | egrep -o "[a-z]+\:\/\/[a-zA-Z0-9.]+(.com|.cn|.org)+")

echo Downloader $url
curl -s $url | egrep -o "<img src=[^>]*>" | sed 's/<img src=\"\([^"]*\).*/\1/g' > /tmp/url_list.log

sed -i "s|^/|$baseurl/|" /tmp/url_list.log

cd $directory

while read filename;
do
        echo Downloader $filename
        curl -s -O "$filename" --silent

done < /tmp/url_list.log
rm -rf /tmp/url_list.log
