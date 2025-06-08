# PiOven
## A utility to monitor, log, and analyze tempertures in Raspberry Pi OS
PiOven is a utility that allows you to actively monitor, log, and analyze tempertures on any device running Raspberry Pi OS. It enables you to set-and-forget, collecting data for any length of time, then revisiting that data when you are ready to see results.

### Getting Started
1. Clone the project repo
    ```bash
    git clone <repo-url>
    ```
1. Change to the PiOven directory
    ```bash
    cd PiOven
    ```
1. Make the `monitor_temp` script executable
    ```bash
    chmod +x monitor_temp.sh
    ```
1. (Optional) Adjust the sampling interval in the `monitor_temp` script
    - Open the file for editing:
        ```bash
        nano monitor_temp.sh
        ```
    - Change `MONITOR_INTERVAL` to the desired sampling interval, in seconds:
        ```bash
        MONITOR_INTERVAL=<Desired time between samples in seconds>
        ```
    - Save the file by with `ctrl+O`
    - Exit the editor with `ctrl+X`
1. Use the command `make help` to show usage

