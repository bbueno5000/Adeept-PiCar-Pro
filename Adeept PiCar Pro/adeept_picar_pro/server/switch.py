#!/usr/bin/env/python

# File name   : switch.py
# Production  : HAT
# Website     : www.gewbot.com
# Author      : William
# Date        : 2018/08/22

import RPi.GPIO as GPIO
import time

def set_all_switch_off():
    """
    TODO: docstring
    """
    switch(1,0)
    switch(2,0)
    switch(3,0)

def switch(port, status):
    """
    TODO: docstring
    """
    if port == 1:
        if status == 1:
            GPIO.output(5, GPIO.HIGH)
        elif status == 0:
            GPIO.output(5,GPIO.LOW)
        else:
            pass
    elif port == 2:
        if status == 1:
            GPIO.output(6, GPIO.HIGH)
        elif status == 0:
            GPIO.output(6,GPIO.LOW)
        else:
            pass
    elif port == 3:
        if status == 1:
            GPIO.output(13, GPIO.HIGH)
        elif status == 0:
            GPIO.output(13,GPIO.LOW)
        else:
            pass
    else:
        print('Wrong Command: Example--switch(3, 1)->to switch on port3')

def switchSetup():
    """
    TODO: docstring
    """
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)


if __name__ == "__main__":
    switchSetup()
    while 1:
        switch(1,1)
        switch(2,1)
        switch(3,1)
        print("Light on...")
        time.sleep(1)
        set_all_switch_off()
        print("Light off...")
        time.sleep(1)