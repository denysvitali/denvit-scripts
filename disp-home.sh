#!/bin/bash

xrandr --listactivemonitors | grep eDP-1 > /dev/null
intel_test=$?

if [ $intel_test != 0 ]; then
    echo "Intel"
    ~/.screenlayout/home-intel.sh
else
    echo "Modesetting"
    ~/.screenlayout/home.sh
fi;

~/scripts/apply-screen.sh
