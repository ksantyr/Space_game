import cv2
import numpy as np

# Función para detectar el color naranja en la imagen
def color_naranja(frame):
    # Definir el rango de color naranja en formato HSV
    inferior = np.array([5, 100, 100])  # Valor mínimo de matiz, saturación y valor
    superior = np.array([15, 255, 255])  # Valor máximo de matiz, saturación y valor

    # Convertir la imagen a espacio de color HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Crear una máscara para el color naranja
    mascara = cv2.inRange(hsv, inferior, superior)

    return mascara

# Inicializar la cámara
camara = cv2.VideoCapture(0)

# Configurar el tamaño del fotograma capturado
camara.set(3, 400)
camara.set(4, 400)

# lectura
while True: 
    ret, frame = camara.read()

    if not ret:
        break

    # Detectar el color naranja en el fotograma actual
    mascara = color_naranja(frame)

    # Encontrar los contornos en la máscara de color naranja
    contorno, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for i in contorno:

        # Calcular el área del contorno
        area = cv2.contourArea(i)

        if area > 1000:  # Cambia este valor según tu entorno
            # Encontrar el rectángulo que enmarca el área de detección naranja
            x, y, w, h = cv2.boundingRect(i)

            # Dibujar un cuadro alrededor del área de detección naranja en el fotograma original
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 165, 255), 2)  # Naranja en formato BGR

    # Crear una imagen binaria donde el objeto naranja es blanco y el resto negro
    binario = cv2.bitwise_and(frame, frame, mask=mascara)

    # Mostrar dos ventanas separadas: una con la detección de color naranja y otra con la imagen binaria
    cv2.imshow("Orange Color Detection", frame)
    cv2.imshow("Orange Binary Image", binario)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
camara.release()
cv2.destroyAllWindows()
cv2.AllWindows()