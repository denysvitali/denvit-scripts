#!/usr/bin/bash

export DISPLAY=:0
export XAUTHORITY=/home/$USERNAME/.Xauthority

set -e
MONITOR='HDMI-A-2'

function logger {
  echo $1 $2
}

function wait_for_monitor {
    xrandr | grep $MONITOR | grep '\bconnected'
    while [ $? -ne 0 ]; do
            logger -t "waiting for 100ms"
            sleep 0.1
            xrandr | grep $MONITOR | grep '\bconnected'
    done
 }

EXTERNAL_MONITOR_STATUS=$(cat /sys/class/drm/card0-$MONITOR/status )
if [ $EXTERNAL_MONITOR_STATUS  == "connected" ]; then
    wait_for_monitor
    xrandr --output $MONITOR --auto --primary --output eDP-1 --auto --left-of $MONITOR
    #/home/$USERNAME/bin/i3plug.py restore
else
    #/home/$USERNAME/bin/i3plug.py save
    xrandr --output $MONITOR --off
fi
nitrogen --restore && ~/.config/polybar/launch.sh
