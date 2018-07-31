#!/bin/bash

xrandr --listactivemonitors | grep eDP-1 > /dev/null
intel_test=$?

if [ $intel_test != 0 ]; then
    echo "Intel"
    ~/.screenlayout/work-intel.sh
else
    echo "Modesetting"
    ~/.screenlayout/work.sh
fi;

~/scripts/apply-screen.sh
