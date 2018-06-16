#!/bin/sh

if [ -z "$1" ]; then
  echo "Please, provide a BT address."
  exit;
fi

bluetoothctl power on
bluetoothctl connect $1
