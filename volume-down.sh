#!/bin/sh
DEFAULT_SINK=$(pacmd stat | awk -F ": " '/^Default sink name: /{print $2}')
pactl set-sink-volume $DEFAULT_SINK -2%
