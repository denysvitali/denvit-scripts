#!/bin/sh
sed -Ei 's@<text.*?>UNREGISTERED</text>@@g' $1
