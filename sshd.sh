#!/bin/bash
# Specific script. Sets resolution of second screen to support large values.
# Used for SUNVIEW TV.

xrandr --newmode "1656x900_60.00" 122.25 1656 1752 1920 2184 900 903 913 934 -hsync +vsync
xrandr --addmode VGA-1 1656x900_60.00
