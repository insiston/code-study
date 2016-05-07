#!/bin/bash

bak_from_name="etc"               
bak_from_dir="/etc"               
bak_to_dir="/var/backup"          
bak_dir="${bak_to_dir}${bak_from_dir}.$(date +%Y%m%d)"                        
day_bak_dir="${bak_to_dir}${bak_from_dir}.$(date -d '-1 day' +%Y%m%d)"        
new_md5_file="${bak_to_dir}/new_md5.$bak_from_name.$(date +%Y%m%d)"           
old_md5_file="${bak_to_dir}/old_md5.$bak_from_name.md5"                       

if [ ! -d $bak_to_dir ]
    then
    mkdir $bak_from_dir
fi

find $bak_from_dir | xargs -I {} md5sum {} >> $new_md5_file 2>/dev/null
cp -a $bak_from_dir $bak_to_dir

if [ $? -eq 0]
    then
echo "$bak_from_dir directory to $bak_to_dir backup successfull"
fi

new_md5_error=`md5sum -c $new_md5_file 2>/dev/null | awk '$2 !~ "ok"' | wc -l`             
new_md5_ok=`md5sum -c $new_md5_file 2>/dev/null | awk '$2 !~ "ok"' | wc -l`                
old_md5_error=`md5sum -c $old_md5_file 2>/dev/null | awk '$2 !~ "ok"' | wc -l`             
old_md5_ok=`md5sum -c $old_md5_file 2>/dev/null | awk '$2 !~ "ok"' | wc -l`                

if [ $new_md5_error == $old_md5_error -a $new_md5_ok == $old_md5_ok ]
    then
    echo "Because today and yesterday's content is the same, delete the backup content of yesterday"
    rm -rf $day_bak_dir $new_md5_file
fi

echo | cp $new_md5_file $old_md5_file &>/dev/null



