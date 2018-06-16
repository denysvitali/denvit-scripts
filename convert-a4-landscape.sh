#!/bin/bash
string=""
newline=$(echo -e "\n")
output=$1
shift
for i in $@; do
  echo $i;
  string="$string($i) viewJPEG showpage$newline"
done
gs -sDEVICE=pdfwrite -sPAPERSIZE=a4 -dORIENT1=false -o ${output} /usr/share/ghostscript/9.22/lib/viewjpeg.ps -c "${string}"
