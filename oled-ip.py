#oled-ip.py

import time
import sys
import socket
import fcntl
import struct
from time import sleep

import Adafruit_SSD1306


# Sets our variables to be used later
RST = 24
TEXT = ''


# 96x16 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_96_16(rst=RST)

# Initialize library.
disp.begin()
disp.clear()

# This function allows us to grab any of our IP addresses
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

# This sets TEXT equal to whatever your IP address is, or isn't
try:
    TEXT = get_ip_address('wlan0') # WiFi address of WiFi adapter. NOT ETHERNET
except IOError:
    try:
        TEXT = get_ip_address('eth0') # WiFi address of Ethernet cable. NOT ADAPTER
    except IOError:
        TEXT = ('NO INTERNET!')

# The actual printing of TEXT
disp.clear()
intro = 'Hello!'
ip = 'Your IP Address is:'
disp.draw_text2(0,25,TEXT,1)
disp.draw_text2(0,0,intro,2)
disp.draw_text2(0,16, ip, 1)
disp.display()
