#!/usr/bin/env python

#import camera driver
from camera_opencv import Camera
#from camera_pi import Camera # Raspberry Pi camera module (requires picamera package)
from flask import Flask, render_template, Response, send_from_directory
from flask_cors import *
from importlib import import_module
import os
import threading

app = Flask(__name__)

CORS(app, supports_credentials=True)

camera = Camera()

dir_path = os.path.dirname(os.path.realpath(__file__))

def gen(camera):
    """
    Video streaming generator function.
    """
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    """
    TODO: docstring
    """
    return send_from_directory(dir_path + '/dist', 'index.html')

@app.route('/css/<path:filename>')
def sendcss(filename):
    """
    TODO: docstring
    """
    return send_from_directory(dir_path + '/dist/css', filename)

@app.route('/fonts/<path:filename>')
def sendfonts(filename):
    """
    TODO: docstring
    """
    return send_from_directory(dir_path + '/dist/fonts', filename)

@app.route('/<path:filename>')
def sendgen(filename):
    """
    TODO: docstring
    """
    return send_from_directory(dir_path + '/dist', filename)

@app.route('/api/img/icon/<path:filename>')
def sendicon(filename):
    """
    TODO: docstring
    """
    return send_from_directory(dir_path + '/dist/img/icon', filename)

@app.route('/api/img/<path:filename>')
def sendimg(filename):
    """
    TODO: docstring
    """
    return send_from_directory(dir_path+'/dist/img', filename)

@app.route('/js/<path:filename>')
def sendjs(filename):
    """
    TODO: docstring
    """
    return send_from_directory(dir_path+'/dist/js', filename)

@app.route('/video_feed')
def video_feed():
    """
    Video streaming route. Put this in the src attribute of an img tag.
    """
    return Response(gen(camera), mimetype='multipart/x-mixed-replace; boundary=frame')

class webapp:
    """
    TODO: docstring
    """
    def __init__(self):
        """
        TODO: docstring
        """
        self.camera = camera

    def colorFindSet(self, H, S, V):
        """
        TODO: docstring
        """
        camera.colorFindSet(H, S, V)

    def modeselect(self, modeInput):
        """
        TODO: docstring
        """
        Camera.modeSelect = modeInput

    def startthread(self):
        """
        TODO: docstring
        """
        fps_threading = threading.Thread(target=self.thread) # define a thread for FPV and OpenCV
        fps_threading.setDaemon(False) # 'True' means it is a front thread, it would close when the mainloop() closes
        fps_threading.start() # thread starts

    def thread(self):
        """
        TODO: docstring
        """
        app.run(host='0.0.0.0', threaded=True)
