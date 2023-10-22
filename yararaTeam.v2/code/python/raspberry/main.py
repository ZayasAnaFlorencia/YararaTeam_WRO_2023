from picam import *

from proceso import dibujar,es_mismo_objeto,calcular_centroide

# from capturaImagen import capturar_imagen

ultimo_objeto_verde = None

umbral_distancia = 100

while True:

    frame = next(obtener_frame())

    #procesamiento / deteccion

    # Convierte el fotograma a espacio de color HSV

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

     # Crea máscaras para los colores rojo y verde

    mask_red = cv2.inRange(hsv, lower_red, upper_red)

    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)

    # Combina las máscaras utilizando el operador OR lógico

    mask_red = cv2.bitwise_or(mask_red, mask_red2)

    mask_green = cv2.inRange(hsv, lower_green, upper_green)



    

    # Encuentra los contornos de los objetos rojos y verdes

    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #dibujar 

    

    dibujar(frame, mask_red, (0, 0, 255))

    

    for contour in contours_green:

        if es_mismo_objeto(contour, ultimo_objeto_verde, umbral_distancia):

            continue  # Es el mismo objeto, no lo proceses

        else:

            # Almacena el nuevo objeto verde en "ultimo_objeto_verde" y procesa

            # el objeto si es diferente

            nuevo_objeto_verde = {

                'centroide': calcular_centroide(contour),

                # Otras propiedades que desees almacenar

            }

            # objetos_verdes.append(nuevo_objeto_verde)

            # Procesa el objeto verde

            dibujar(frame, mask_green, (0, 255, 0))

    # Muestra el fotograma





    cv2.imshow('Detector de colores', frame)

    if cv2.waitKey(50) & 0xFF == ord('s'):

        break



cap.release()

cv2.destroyAllWindows()

