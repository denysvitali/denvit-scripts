#!/bin/bash
xrandr --listactivemonitors | grep eDP-1 > /dev/null
intel_test=$?

if [ $intel_test != 0 ]; then
    echo "Intel"
    ~/.screenlayout/supsi-179-intel.sh
else
    echo "Modesetting"
    ~/.screenlayout/supsi-179.sh
fi;
~/scripts/apply-screen.sh
