#!/bin/bash
# Initial setup for ROS Scripts, this script must be launched once to create
# "config" folder and puopulate it with necessary files.

mkdir "../config"
echo "http://127.0.0.1:11311" > "../config/master_uri.conf"
echo "127.0.0.1" > "../config/ros_ip.conf"
echo "DEFAULT" > "../config/device.conf"
echo "Configuration complete."
