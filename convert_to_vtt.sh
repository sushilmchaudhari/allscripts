#!/bin/bash

text_file="/tmp/test2"

first_word="items:"
while read line 
do
   if [[ "$line" =~ ^"$first_word" ]]
   then
        start_time=`echo $line | cut -d, -f1 | cut -d: -f3`
        end_time=`echo $line | cut -d, -f2 | cut -d: -f2`
   else
   	start_time=`echo $line | cut -d, -f1 | cut -d: -f2`
	end_time=`echo $line | cut -d, -f2 | cut -d: -f2`
   fi

done < $text_file



