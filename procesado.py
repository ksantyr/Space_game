import cv2
import numpy as np


# Función para detectar el color en la imagen
def color(frame, tamaño):

    # Definir un rango de color verde en HSV, color de referencia
    inferior = np.array([60, 100, 20],np.uint8)  # Matiz mínimo, Saturación mínima, Valor mínimo [164,61,71]    [35, 90, 20]
    superior = np.array([90, 255, 255],np.uint8)  # Matiz máximo, Saturación máxima, Valor máximo [164,61,71]   [85, 255, 255]

    # Redimensionar el fotograma al tamaño personalizado
    frame_redimensionado = cv2.resize(frame, tamaño)

    # Aplicar espejado horizontal (modo espejo)
    frame_espejo = cv2.flip(frame_redimensionado, 1)
    
    # Convertir la imagen a espacio de color HSV
    hsv = cv2.cvtColor(frame_espejo, cv2.COLOR_BGR2HSV)

    # Crear una máscara para el color naranja
    mascara = cv2.inRange(hsv, inferior, superior)

    return mascara, frame_espejo, hsv

#Coordenadas del objeto
cX = 0
cY= 0

def lectura(jugador, tamano, camara):
# lectura
    ret, frame = camara.read()
    run = True
    if not ret:
        print("Error: No se pudo leer el fotograma de la cámara.")
        run=False

    # Detectar el color naranja en el fotograma actual
    mascara, frame_espejo, hsv  = color(frame,tamano)

    # Encontrar los contornos en la máscara de color naranja
    contornos, _ = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contorno in contornos:

        # Calcular el área del contorno
        area = cv2.contourArea(contorno)

        if area > 2000:  # Desprecia los objetos pequeños para segmentar el deseado
            M = cv2.moments(contorno)
            if M["m00"] == 0: M["m00"] =1 #Para evitar divisiones por cero
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            # Dibujar un círculo en el centro del objeto naranja
            cv2.circle(frame_espejo, (cX, cY), 7, (255, 255, 255), -1)
            

            # Mostrar las direcciones detectadas en la pantalla
            cv2.putText(frame_espejo, f"Direccion X: {cX}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            cv2.putText(frame_espejo, f"Direccion Y: {cY}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            
            #Actualizar Jugador 
            #...............
            jugador.posicion(cX,cY)
            #sprites.update(ventana)

    # Crear una imagen binaria donde el objeto naranja es blanco y el resto negro
    binario = cv2.bitwise_and(hsv, hsv, mask=mascara)

    # Mostrar dos ventanas separadas: una con la detección de color naranja y otra con la imagen binaria
    cv2.imshow("Orange Color Detection", frame_espejo)
    cv2.imshow("Orange Binary Image", binario)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        run=False

    return run
    
    

