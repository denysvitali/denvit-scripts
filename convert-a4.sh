#!/bin/bash
string=""
newline=$(echo -e "\n")
output=$1
shift
for i in $@; do
  echo $i;
  string="$string($i) viewJPEG showpage$newline"
done
gs -sDEVICE=pdfwrite -sPAPERSIZE=a4 -o ${output} /usr/share/ghostscript/*/lib/viewjpeg.ps -c "${string}"
