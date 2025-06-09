#! /bin/bash

MONITOR_INTERVAL=1

# Forever sample CPU temperature, direct output to temperature log file
while true; do
    vcgencmd measure_temp >> temperature.log
    sleep $MONITOR_INTERVAL
done