#!/bin/bash
intern=eDP-1
extern=HDMI-1

xrandr --output "$intern" --auto --output "$extern" --auto --same-as "$intern"
~/scripts/apply-screen.sh
