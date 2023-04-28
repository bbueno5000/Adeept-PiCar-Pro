#!/usr/bin/env/python

# File name   : server.py
# Production  : Gtank
# Website     : www.gewbot.com
# E-mail      : gewubot@163.com
# Author      : William
# Date        : 2019/10/28

import LED
import move
import os
import servo
import socket
import switch
import threading
import time

servo.servo_init()
switch.switchSetup()
switch.set_all_switch_off()
LED  = LED.LED()
LED.colorWipe(80,255,0)
step_set = 1
speed_set = 100
rad = 0.6
direction_command = 'no'
turn_command = 'no'
servo_command = 'no'
pos_input = 1
catch_input = 1
cir_input = 6
servo_speed  = 11

def app_ctrl():
    """
    TODO: docstring
    """
    global servo_move
    app_HOST = ''
    app_PORT = 10123
    app_BUFSIZ = 1024
    app_ADDR = (app_HOST, app_PORT)
    servo_move = Servo_ctrl()
    servo_move.start()
    servo_move.pause()
    appconnect()
    setup()
    app_threading=threading.Thread(target=appconnect) # define a thread for FPV and OpenCV
    app_threading.setDaemon(True) # 'True' means it is a front thread, it would close when the mainloop() closes
    app_threading.start() # thread starts
    while 1:
        data = ''
        data = str(AppCliSock.recv(app_BUFSIZ).decode())
        if not data:
            continue
        appCommand(data)
        pass

    def appCommand(data_input):
        """
        TODO: docstring
        """
        global direction_command, turn_command, servo_command
        if data_input == 'forwardStart\n':
            direction_command = 'forward'
            move.move(speed_set, direction_command, turn_command, rad)
        elif data_input == 'backwardStart\n':
            direction_command = 'backward'
            move.move(speed_set, direction_command, turn_command, rad)
        elif data_input == 'leftStart\n':
            turn_command = 'left'
            move.move(speed_set, direction_command, turn_command, rad)
        elif data_input == 'rightStart\n':
            turn_command = 'right'
            move.move(speed_set, direction_command, turn_command, rad)
        elif 'forwardStop' in data_input:
            direction_command = 'no'
            move.move(speed_set, direction_command, turn_command, rad)
        elif 'backwardStop' in data_input:
            direction_command = 'no'
            move.move(speed_set, direction_command, turn_command, rad)
        elif 'leftStop' in data_input:
            turn_command = 'no'
            move.move(speed_set, direction_command, turn_command, rad)
        elif 'rightStop' in data_input:
            turn_command = 'no'
            move.move(speed_set, direction_command, turn_command, rad)
        if data_input == 'lookLeftStart\n':
            servo_command = 'lookleft'
            servo_move.resume()
        elif data_input == 'lookRightStart\n': 
            servo_command = 'lookright'
            servo_move.resume()
        elif data_input == 'downStart\n':
            servo_command = 'down'
            servo_move.resume()
        elif data_input == 'upStart\n':
            servo_command = 'up'
            servo_move.resume()
        elif 'lookLeftStop' in data_input:
            servo_move.pause()
            servo_command = 'no'
        elif 'lookRightStop' in data_input:
            servo_move.pause()
            servo_command = 'no'
        elif 'downStop' in data_input:
            servo_move.pause()
            servo_command = 'no'
        elif 'upStop' in data_input:
            servo_move.pause()
            servo_command = 'no'
        if data_input == 'aStart\n':
            servo_command = 'grab'
            servo_move.resume()
        elif data_input == 'bStart\n':
            servo_command = 'loose'
            servo_move.resume()
        elif data_input == 'cStart\n':
            switch.switch(1,1)
            switch.switch(2,1)
            switch.switch(3,1)
        elif data_input == 'dStart\n':
            switch.switch(1,0)
            switch.switch(2,0)
            switch.switch(3,0)
        elif 'aStop' in data_input:
            servo_move.pause()
            servo_command = 'no'
        elif 'bStop' in data_input:
            servo_move.pause()
            servo_command = 'no'
        elif 'cStop' in data_input:
            pass
        elif 'dStop' in data_input:
            pass
        print(data_input)

    def appconnect():
        """
        TODO: docstring
        """
        global AppCliSock, AppAddr
        try:
            s =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            s.connect(("1.1.1.1",80))
            ipaddr_check=s.getsockname()[0]
            s.close()
            print(ipaddr_check)
            AppSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            AppSerSock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            AppSerSock.bind(app_ADDR)
            AppSerSock.listen(5)
            print('waiting for App connection...')
            AppCliSock, AppAddr = AppSerSock.accept()
            print('...App connected from :', AppAddr)
        except:
            ap_threading=threading.Thread(target=ap_thread) # define a thread for data receiving
            ap_threading.setDaemon(True) # 'True' means it is a front thread, it would close when the mainloop() closes
            ap_threading.start() # thread starts
            LED.colorWipe(0, 16, 50)
            time.sleep(1)
            LED.colorWipe(0, 16, 100)
            time.sleep(1)
            LED.colorWipe(0, 16, 150)
            time.sleep(1)
            LED.colorWipe(0, 16, 200)
            time.sleep(1)
            LED.colorWipe(0, 16, 255)
            time.sleep(1)
            LED.colorWipe(35, 255, 35)
            AppSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            AppSerSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            AppSerSock.bind(app_ADDR)
            AppSerSock.listen(5)
            print('waiting for App connection...')
            AppCliSock, AppAddr = AppSerSock.accept()
            print('...App connected from :', AppAddr)

    def ap_thread():
        """
        TODO: docstring
        """
        os.system("sudo create_ap wlan0 eth0 Groovy 12345678")

    def setup():
        """
        TODO: docstring
        """
        move.setup()

class Servo_ctrl(threading.Thread):
    """
    TODO: docstring
    """
    def __init__(self, *args, **kwargs):
        """
        TODO: docstring
        """
        super(Servo_ctrl, self).__init__(*args, **kwargs)
        self.__flag = threading.Event() # the flag used to suspend the thread
        self.__flag.set() # set as True
        self.__running = threading.Event() # flag used to stop the thread
        self.__running.set() # will running set as True

    def pause(self):
        """
        TODO: docstring
        """
        self.__flag.clear() # set as False, let the thread block

    def resume(self):
        """
        TODO: docstring
        """
        self.__flag.set() # set as True, let the thread stop blocking

    def run(self):
        """
        TODO: docstring
        """
        while self.__running.isSet():
            self.__flag.wait() # for True return immediately when, for False block until the internal flag is True return after
            if servo_command == 'lookleft':
                servo.lookleft(servo_speed)
            elif servo_command == 'lookright':
                servo.lookright(servo_speed)
            elif servo_command == 'up':
                servo.up(servo_speed)
            elif servo_command == 'down':
                servo.down(servo_speed)
            elif servo_command == 'lookup':
                servo.lookup(servo_speed)
            elif servo_command == 'lookdown':
                servo.lookdown(servo_speed)
            elif servo_command == 'grab':
                servo.grab(servo_speed)
            elif servo_command == 'loose':
                servo.loose(servo_speed)
            else:
                pass
            time.sleep(0.07)

    def stop(self):
        """
        TODO: docstring
        """
        self.__flag.set() # Resume a thread from a suspended state, how have paused words
        self.__running.clear() # set as False  

AppConntect_threading=threading.Thread(target=app_ctrl) # define a thread for FPV and OpenCV
AppConntect_threading.setDaemon(True) # 'True' means it is a front thread, it would close when the mainloop() closes
AppConntect_threading.start() # thread starts


if __name__ == '__main__':
    i = 1
    try:
        while 1:
            i += 1
            print(i)
            time.sleep(30)
            pass
    except:
        servo_move.stop()
        move.move(0, 'no', 'no', rad)
        LED.colorWipe(0, 0, 0)
