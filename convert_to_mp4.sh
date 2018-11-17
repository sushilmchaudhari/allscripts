#!/usr/bin/env bash

BASENAME=$0
VID_PATH="/var/sv/msri"
SUCCESS=0
OUTFILE="/tmp/list.txt"

print_usage() {
  ERROR_MSG="$1"

  if [ "$ERROR_MSG" != "" ]; then
    echo "ERROR: $ERROR_MSG" 1>&2
  fi

  echo ""
  echo "Usage:" 
  echo "       $BASENAME 1993"
  echo ""
  echo "  The argument to the script must be an year from the list"
  echo "  - 1993  1996  1997  1998  1999  2000  2001  2002  2003  2004"
  echo ""
} # end print_usage

# Vaildate number of parameters
if [ "$#" -ne 1 ]; then
  print_usage "Argument required"
  exit 1
fi

# Validate 1st parameter
if [ -z "$1" ]; then
  print_usage "Must specify the envirnoment, such as prod or staging"
  exit 1
fi
INSTANCE_ENV=$1

YEAR=$1

echo "Finding real media video files from the year $YEAR"
find $VID_PATH/$YEAR/ -type f -iname "*.rm" > $OUTFILE 2> /dev/null
if [ "$?" -ne $SUCCESS ]
then
   echo "Unable to locate $VID_PATH/$YEAR. Please check year entered."
   exit $?
fi 

echo "Starting conversion of .rm to .mp4"

while read line
do
   source_dir=`echo $line | rev | cut -d/ -f2- | rev`
   file_name=`echo $line | awk -F '/' '{print $NF}' | cut -d. -f1`
   echo "File name is : $file_name "
   echo "Converting $line to mp4 ... "
#   /usr/bin/ffmpeg -i $line -strict -2 "$source_dir"/"$file_name".mp4
   if [ "$?" -ne $SUCCESS ]
   then
      echo "Unable to convert file $line to .mp4"
   else
      echo "File $line successfully converted to .mp4"
   fi
done < $OUTFILE
