#!/usr/bin/python3

import os
import time

curpath = os.path.realpath(__file__)
thisPath = "/" + os.path.dirname(curpath)

for x in range(1, 4):
    if os.system("sudo apt update") == 0:
        break

os.system("sudo apt purge -y wolfram-engine")
os.system("sudo apt purge -y libreoffice*")
os.system("sudo apt -y clean")
os.system("sudo apt -y autoremove")

for _ in range(1, 4):
    if os.system("sudo apt install -y python3-pip") == 0:
        break

for _ in range(1, 4):
    if os.system("sudo pip3 install adafruit-pca9685") == 0:
        break

for _ in range(1, 4):
    if os.system("sudo pip3 install psutil") == 0:
        break

for _ in range(1, 4):
    if os.system("sudo pip3 install websockets") == 0:
        break

for _ in range(1, 4):
    if os.system("sudo pip3 install flask") == 0:
        break

for _ in range(1, 4):
    if os.system("sudo pip3 install flask_cors") == 0:
        break

for _ in range(1, 4):
    if os.system("sudo apt install -y libharfbuzz0b") == 0:
        break

for _ in range(1, 4):
    if os.system("sudo apt install -y libilmbase-dev") == 0:
        break

for _ in range(1, 4):
    if os.system("sudo apt install -y libopenexr-dev") == 0:
        break

for _ in range(1, 4):
    if os.system("sudo apt install -y libgstreamer1.0-dev") == 0:
        break

for _ in range(1, 4):
    if os.system("sudo apt install -y libavcodec-dev") == 0:
        break

for _ in range(1, 4):
    if os.system("sudo apt install -y libavformat-dev") == 0:
        break

for _ in range(1, 4):
    if os.system("sudo apt install -y libswscale-dev") == 0:
        break

for _ in range(1, 4):
    if os.system("sudo apt install -y libv4l-dev") == 0:
        break

for _ in range(1, 4):
    if os.system("sudo apt install -y libxvidcore-dev") == 0:
        break

for _ in range(1, 4):
    if os.system("sudo apt install -y libx264-dev") == 0:
        break

for _ in range(1, 4):
    if os.system("sudo apt install -y libdc1394-22-dev") == 0:
        break

for _ in range(1, 4):
    if os.system("sudo apt install -y libgstreamer-plugins-base1.0-dev") == 0:
        break

for _ in range(1, 4):
    if os.system("sudo pip3 install imutils") == 0:
        break

for _ in range(1, 4):
    if os.system("sudo pip3 install luma.oled") == 0:
        break

for _ in range(1, 4):
    if os.system("sudo apt-get install -y i2c-tools") == 0:
        break

for _ in range(1, 4):
    if os.system("sudo pip3 install rpi_ws281x") == 0:
        break

for _ in range(1, 4):
    if os.system("sudo pip3 install opencv-contrib-python==3.4.3.18") == 0:
        break

for _ in range(1, 4):
    if os.system("sudo pip3 install mpu6050-raspberrypi") == 0:
        break

for _ in range(1, 4):
    if os.system("sudo apt install -y python3-smbus") == 0:
        break

for _ in range(1, 4):
    if os.system("sudo apt install -y libjpeg-dev") == 0:
        break

try:
    replace_num("/boot/config.txt", '#dtparam=i2c_arm=on', 'dtparam=i2c_arm=on\nstart_x=1\n')
except:
    print('try again')

try:
    os.system('sudo touch //home/pi/startup.sh')
    with open("//home/pi/startup.sh", 'w') as file_to_write:
        file_to_write.write("#!/bin/sh\nsudo python3 " + thisPath + "/server/webServer.py")
        # file_to_write.write("#!/bin/sh\nsudo python3 " + thisPath + "/server/server.py")
except:
    pass

os.system('sudo chmod 777 //home/pi/startup.sh')
replace_num('/etc/rc.local', 'fi', 'fi\n//home/pi/startup.sh start')
print('The program in Raspberry Pi has been installed, disconnected and restarted. \nYou can now power off the Raspberry Pi to install the camera and driver board (Robot HAT). \nAfter turning on again, the Raspberry Pi will automatically run the program to set the servos port signal to turn the servos to the middle position, which is convenient for mechanical assembly.')
print('restarting...')
os.system("sudo reboot")

def replace_num(file, initial, new_num):
    """
    TODO: docstring
    """
    newline = ""
    str_num = str(new_num)
    with open(file, "r") as f:
        for line in f.readlines():
            if line.find(initial) == 0:
                line = str_num + '\n'
            newline += line
    with open(file, "w") as f:
        f.writelines(newline)
