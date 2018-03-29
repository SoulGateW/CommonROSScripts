#!/usr/bin/env python

# Monitor script for ssh session from Android smartphone.
# Keeps the output in 30 characters wide!

import subprocess
import signal
import time
import sys

def sigint_handler(signal, frame):
    print ""
    print "Keyboard interrupt!"
    print "Monitor terminated."
    sys.exit(0)

if __name__ == '__main__':
    # Clear the screen
    print(chr(27) + "[2J")

    # Register SIGINT handler
    signal.signal(signal.SIGINT, sigint_handler)

    # Main endless cycle
    while True:
        # Getting the "top" output
        res = subprocess.check_output(['top','-bcn1','-w512'])
        res = res.split("\n")

        line_no = 0
        consuming_count = 1

        # Clear the screen
        print(chr(27) + "[2J")

        #Move to top right corner of the screen
        print('\033[1;1H')
        print "MONITORING:"
        print ""

        for line in res:
            if (line_no < 15) and (line_no > 30):
                print line_no, ':', line

            #Uptime, users and load average
            if line_no == 0:
                data = line.split()
                #Date and time
                time_uptime = data[2] + " uptime: "+ data[4].replace(",","")
                print "Time :",time_uptime
                print ""
                #Load
                load_1m  = data[10]
                load_5m  = data[11]
                load_15m = data[12]
                print "Load : %s %s %s" % (load_1m, load_5m, load_15m)

            #CPU
            if line_no == 2:
                data = line.split()
                # CPU Idle
                idle = data[7]
                idle = idle.replace(",",".")
                idle_value = float(idle)
                busy_value = 100.0-idle_value
                #print "CPU  : %0.1f%%" % (busy_value)
                print ""

            # Memory
            if line_no == 3:
                data = line.split()
                total_mem = int(data[3])
                total_mem_mb = total_mem / 1024.0
                free_mem = int(data[5])
                free_mem_mb = free_mem / 1024.0
                print "MEM  : %7.2f / %7.2f MB" % (free_mem_mb, total_mem_mb)

            # Swap
            if line_no == 4:
                data = line.split()
                total_mem = int(data[2])
                total_mem_mb = total_mem / 1024.0
                free_mem = int(data[4])
                free_mem_mb = free_mem / 1024.0
                print "SWAP : %7.2f / %7.2f MB" % (free_mem_mb, total_mem_mb)

            # List most consuming processes
            if (line_no == 7):
                print ""
                print "%5s %5s %5s %10s" % ("ID", "CPU", "MEM", "process")
            if (line_no >= 7) and (line_no <= 12):
                data = line.split()
                print "%5s %5s %5s %.14s" % (data[0], data[8], data[9], data[11])
                consuming_count = consuming_count + 1

            line_no = line_no + 1

        time.sleep(1)
