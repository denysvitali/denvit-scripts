#!/bin/bash
xrandr --listactivemonitors | grep eDP-1 > /dev/null
intel_test=$?

if [ $intel_test != 0 ]; then
    echo "Intel"
    ~/.screenlayout/nb-only-intel.sh
else
    echo "Modesetting"
    ~/.screenlayout/nb-only.sh
fi;
~/scripts/apply-screen.sh
