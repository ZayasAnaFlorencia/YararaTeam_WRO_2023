import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 15)

# Define el rango de colores rojo en HSV
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([179, 255, 255])



# Define el rango de colores verde en HSV
lower_green = np.array([40, 40, 40])
upper_green = np.array([80, 255, 255])