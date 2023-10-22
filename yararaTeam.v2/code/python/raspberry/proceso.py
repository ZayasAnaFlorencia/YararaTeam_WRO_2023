import cv2
import numpy as np
# Umbral de distancia para considerar que dos regiones pertenecen al mismo objeto
umbral_distancia = 200

def dibujar(frame, mask, color):
    # Encuentra los contornos en la máscara en escala de grises
    contornos, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contornos:
        area = cv2.contourArea(c)
        if area > 3000:
            if color == (0, 0, 255):
                # combined_contours_red = np.vstack(contours_red)
                # Calcular los rectángulos de límite para los contornos combinados
                epsilon = 0.03 * cv2.arcLength(c, True)  # Ajusta el valor de epsilon según tus necesidades

                approx = cv2.approxPolyDP(c, epsilon, True)
                x, y, w, h = cv2.boundingRect(approx)

                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)  # Rectángulo rojo
                # x_red, y_red, w_red, h_red = cv2.boundingRect(c)

                # Dibujar el rectángulo alrededor de los objetos rojos

                # cv2.rectangle(frame, (x_red, y_red), (x_red + w_red, y_red + h_red), (0, 0, 255), 3)  # Rectángulo rojo

            else:
                M = cv2.moments(c)
                if M["m00"] == 0:
                    M["m00"] = 1

                x = int(M["m10"] / M["m00"])

                y = int(M['m01'] / M['m00'])

                # nuevoContorno = cv2.convexHull(c, returnPoints=True)

                # cv2.drawContours(frame, [nuevoContorno], -1, color, 3)

                cv2.circle(frame, (x, y), 7, (0, 0, 255), -1)

            # cv2.circle(frame, (x, y), 7, color, -1)

            # font = cv2.FONT_HERSHEY_SIMPLEX

            # cv2.putText(frame, '{},{}'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA)

            # x = int(M["m10"] / M["m00"])

            # y = int(M["m01"] / M["m00"])

            # Dibuja el centroide en el frame

            # cv2.circle(frame, (x, y), 7, (0, 0, 255), -1)





def calcular_distancia(contorno, ancho):
    distancia_real = 10.0  # Distancia en centímetros
    ancho_real = 10.0  # Ancho real del objeto en centímetros
    ancho_pixel = 100  # Ancho del objeto en píxeles en la imagen
    distancia = (ancho_real * ancho_pixel) / (2 * ancho_real * np.tan(fov / 2))
    print(ancho)
    return distancia

def calcular_centroide(contorno):
    M = cv2.moments(contorno)
    if M["m00"] == 0:
        M["m00"] = 1
    x = int(M["m10"] / M["m00"])
    y = int(M['m01'] / M['m00'])
    return x, y

def distancia_entre_puntos(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def es_mismo_objeto(contorno1, contorno2, umbral_distancia):
    centroide1 = calcular_centroide(contorno1)
    centroide2 = calcular_centroide(contorno2)
    distancia = distancia_entre_puntos(centroide1, centroide2)
    return distancia < umbral_distancia