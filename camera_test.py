#!/usr/bin/python3

import cv2
import time
from picamera2 import Picamera2, Preview

import sys
import tty
import termios

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# 1. initialize and configure the camera
picam2 = Picamera2()
preview_config = picam2.create_preview_configuration(main={"size": (1920, 1080)})
picam2.configure(preview_config)

# 2. start the camera and preview
picam2.start_preview(Preview.QTGL)
picam2.start()

# 3. setup manual focus
focus=10
picam2.set_controls({'AfMode': 0, 'LensPosition':focus})
print('[1] zoom in, [2] zoom out, [q] quit')
while True:
	key = getch()
	if key == '1':
		focus=min(15,focus+1)
		print(f'[{focus}]')
	elif key == '2':
		focus=max(0,focus-1)
		print(f'[{focus}]')
	elif key == 'q':
		break
	picam2.set_controls({"AfMode": 0, "LensPosition": focus})

# 4. close
picam2.stop()
