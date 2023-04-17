#!/bin/sh --

if [ "$(id -u)" != 0 ]; then
    echo 'Must be ran as root :('
    exit 1
fi

CONTROLLER_MAC=4C:B9:9B:05:D2:83

echo 'Starting bluetoothd'
/etc/init.d/bluetooth start

echo 'Unblocking bluetooth...'
rfkill unblock bluetooth

echo 'Enabling agent...'
bluetoothctl agent on
bluetoothctl default-agent

echo 'Pairing w/ controller...'
bluetoothctl pair $CONTROLLER_MAC
bluetoothctl trust $CONTROLLER_MAC

echo 'Connecting to controller...'
bluetoothctl connect $CONTROLLER_MAC
