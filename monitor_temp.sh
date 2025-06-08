#! /bin/bash

MONITOR_INTERVAL=1

while true; do
    vcgencmd measure_temp >> temperture.log
    sleep $MONITOR_INTERVAL
done