import cv2
import numpy as np
from picamera import PiCamera
from picamera.array import PiRGBArray
import time

# Inicializa la cámara de la Raspberry Pi
camera = PiCamera()
camera.resolution = (320, 240)  # Ajusta la resolución según tus necesidades
rawCapture = PiRGBArray(camera, size=(320, 240))

# Espera un momento para que la cámara se inicie
time.sleep(0.1)

# Define el rango de colores rojo en HSV
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([179, 255, 255])

# Define el rango de colores verde en HSV
lower_green = np.array([40, 40, 40])
upper_green = np.array([80, 255, 255])

def obtener_frame():
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        rawCapture.truncate(0)
        yield image
