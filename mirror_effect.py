import cv2
import os
import time
from matplotlib import pyplot as plt

ruta = os.getcwd() # ruta actual de directorio
lista = os.listdir(ruta) # listado de archivos

# en images se guardaran los nombres de los archivos que terminen con jpg (las imagenes), sin el ".jpg"
images = [x[0:len(x)-4] for x in lista if x[len(x)-3:len(x)] == 'jpg'] 

# en contenido se esta guardando los archivos que teminen con jpg (guarda las imagenes)
contenido = [cv2.imread(x,1) for x in lista if x[len(x)-3:len(x)] == 'jpg']

for i in range(len(images)):
	real = cv2.flip(contenido[i],1) # voltear horizontalmente la imagen
	cv2.imwrite(images[i]+'_volteado.jpg', real) # guardar esas imagenes con su nombre mas '_volteado"

time.sleep(1) # tiempo para que guarde las imagenes

# Actualizar los datos
lista = os.listdir(ruta) 
images = [x[0:len(x)-4] for x in lista if x[len(x)-3:len(x)] == 'jpg'] 
contenido = [cv2.imread(x,1) for x in lista if x[len(x)-3:len(x)] == 'jpg']

for x in range(len(images)):
	plt.subplot(4, 2, x+1) # subplot(row, column, index)
	real = cv2.flip(contenido[x],1) # voltear horizontalmente la imagen
	real = cv2.cvtColor(real, cv2.COLOR_BGR2RGB) # se cambia de BGR a RGB a
	plt.imshow(real)
	if x % 2 == 0:
		plt.title("Original")
	else:
		plt.title("Convertida")
	plt.xticks([]), plt.yticks([]) # change de x and y coordinates

plt.show()

cv2.waitKey(0)
	
cv2.destroyAllWindows()