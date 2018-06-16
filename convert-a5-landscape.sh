#!/bin/bash
newline=$(echo -e "\n")
string=""
orientation="<</Orientation 1>> setpagedevice"
string="$orientation$newline"
output=$1
shift
for i in $@; do
  echo $i;
  string="$string($i) viewJPEG showpage$newline"
done
gs -sDEVICE=pdfwrite -sPAPERSIZE=a5 -o ${output} /usr/share/ghostscript/*/lib/viewjpeg.ps -c "${string}"
