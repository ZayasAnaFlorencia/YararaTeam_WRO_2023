import cv2
import numpy as np


fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

# Función para ajustar el brillo y el contraste
def adjust_brightness_contrast(imagen, brightness, contrast):
    # Aplicar el ajuste de brillo y contraste a la imagen
    adjusted = cv2.convertScaleAbs(imagen, alpha=contrast, beta=brightness)
    return adjusted

# Función para ajustar el Hue (tono), Saturation (saturación) y Value (valor)
def adjust_hsv(hue, saturation, value):
    # Crear una copia de la imagen en formato HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Ajustar los componentes HSV
    hsv[:, :, 0] = np.clip(hue, 0, 179)  # Ajustar el componente Hue (tono)
    hsv[:, :, 1] = np.clip(saturation, 0, 255)  # Ajustar el componente Saturation (saturación)
    hsv[:, :, 2] = np.clip(value, 0, 255)  # Ajustar el componente Value (valor)

    # Convertir la imagen de nuevo a formato BGR
    adjusted = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return adjusted

# Función para detectar un rango de colores en la imagen
def color_detection(hue_min, saturation_min, value_min, hue_max, saturation_max, value_max):
    # Crear una copia de la imagen en formato HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Definir el rango de colores en formato HSV
    lower_bound = np.array([hue_min, saturation_min, value_min])
    upper_bound = np.array([hue_max, saturation_max, value_max])

    # Crear una máscara para los píxeles que están dentro del rango
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    return mask

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Crear una ventana para la imagen
cv2.namedWindow("Ajustes")


# Crear sliders para el brillo y el contraste
cv2.createTrackbar("Brillo", "Ajustes", 0, 1000, lambda x: None)
cv2.createTrackbar("Contraste", "Ajustes", 1, 100, lambda x: None)

# Crear sliders para Hue (tono), Saturation (saturación) y Value (valor)
cv2.createTrackbar("Hue", "Ajustes", 0, 1790, lambda x: None)
cv2.createTrackbar("Saturation", "Ajustes", 0, 2550, lambda x: None)
cv2.createTrackbar("Value", "Ajustes", 0, 2550, lambda x: None)

# Crear sliders para el rango de color
cv2.createTrackbar("Hue min", "Ajustes", 0, 179, lambda x: None)
cv2.createTrackbar("Saturation min", "Ajustes", 0, 255, lambda x: None)
cv2.createTrackbar("Value min", "Ajustes", 0, 255, lambda x: None)
cv2.createTrackbar("Hue max", "Ajustes", 179, 179, lambda x: None)
cv2.createTrackbar("Saturation max", "Ajustes", 255, 255, lambda x: None)
cv2.createTrackbar("Value max", "Ajustes", 255, 255, lambda x: None)

while True:
    # Capturar un cuadro de la cámara
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.rectangle(frame,(0,0),(frame.shape[1],40),(0,0,0),-1)
    color = (0, 255, 0)
    texto_estado = "Estado: No se ha detectado movimiento"
    area_pts = np.array([[150,270], [500,270], [620,frame.shape[0]], [50,frame.shape[0]]])

    

    # Obtendremos la imagen binaria donde la región en blanco representa
    # la existencia de movimiento
    
    # Obtener los valores actuales de brillo y contraste desde los sliders
    brightness = cv2.getTrackbarPos("Brillo", "Ajustes") / 50.0
    contrast = cv2.getTrackbarPos("Contraste", "Ajustes") / 50.0
    
    # Llamar a la función para ajustar brillo y contraste
    adjusted_bc = adjust_brightness_contrast(frame, brightness, contrast)

    # Obtener los valores actuales de Hue (tono), Saturation (saturación) y Value (valor) desde los sliders
    hue = cv2.getTrackbarPos("Hue", "Ajustes")
    saturation = cv2.getTrackbarPos("Saturation", "Ajustes")
    value = cv2.getTrackbarPos("Value", "Ajustes")
    print(f"Valor (Value): {value}")
    # Llamar a la función para ajustar HSV
    adjusted_hsv = adjust_hsv(hue, saturation, value)

    # Obtener los valores actuales del rango de color desde los sliders
    hue_min = cv2.getTrackbarPos("Hue min", "Ajustes")
    saturation_min = cv2.getTrackbarPos("Saturation min", "Ajustes")
    value_min = cv2.getTrackbarPos("Value min", "Ajustes")
    hue_max = cv2.getTrackbarPos("Hue max", "Ajustes")
    saturation_max = cv2.getTrackbarPos("Saturation max", "Ajustes")
    value_max = cv2.getTrackbarPos("Value max", "Ajustes")


    imAux = np.zeros(shape=(frame.shape[:2]), dtype=np.uint8)
    imAux = cv2.drawContours(imAux, [area_pts], -1, (255), -1)
    image_area = cv2.bitwise_and(gray, gray, mask=imAux)
    # Llamar a la función para detectar el rango de color
    color_mask = color_detection(hue_min, saturation_min, value_min, hue_max, saturation_max, value_max)

    # Combinar la imagen ajustada y la máscara de color
    combined_image = cv2.bitwise_and(adjusted_bc, adjusted_hsv, mask=color_mask)
    combined_orig = cv2.bitwise_and(adjusted_bc, adjusted_hsv)
    imag_fin = cv2.bitwise_and(gray, gray, mask=color_mask)
    

    fgmask = fgbg.apply(image_area)
    fgmask = cv2.morphologyEx(imag_fin, cv2.MORPH_OPEN, kernel)
    fgmask = cv2.dilate(imag_fin, None, iterations=2)

    cnts = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for cnt in cnts:
        if cv2.contourArea(cnt) > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x,y), (x+w, y+h),(0,255,0), 2)
            texto_estado = "Estado: Alerta Movimiento Detectado!"
            color = (0, 0, 255) 
    
            cv2.drawContours(frame, [area_pts], -1, color, 2)
            cv2.putText(frame, texto_estado , (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, color,2)

    # Mostrar la imagen combinada
    cv2.imshow("orig", combined_orig)
    cv2.imshow("Ajustes", combined_image)
    cv2.imshow("Final", imag_fin)
    cv2.imshow("ROI", frame)


    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar la ventana
cap.release()
cv2.destroyAllWindows()