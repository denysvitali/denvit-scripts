#!/bin/bash
gs -sDEVICE=pdfwrite -sPAPERSIZE=a4 -o $2 /usr/share/ghostscript/9.22/lib/viewjpeg.ps -c \($1\) viewJPEG
