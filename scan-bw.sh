#!/bin/bash
density=$1
if [ "$density" == "" ]
then
 density=600
fi

device=$(scanimage -L | grep Canon | pcregrep -o1 "device \`(.*?)'")
fnumber=$(find . -type f -regex '^.*/[0-9]+\.jpg$' -exec basename {} \;| sed 's/\([0-9]\+\).*/\1/g' | sort -n | tail -1)
fnumber=$(($fnumber + 1))
echo "Scanning page ${fnumber}"
scanimage -d "$device" --resolution "$density" --mode=Gray --format=jpeg > $fnumber.jpg; convert -rotate 180 $fnumber.jpg -gravity East -crop 4960x7016+0+0 -brightness-contrast 0x20 ${fnumber}_tmp.jpg; mv ${fnumber}_tmp.jpg $fnumber.jpg;
