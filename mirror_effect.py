import cv2
import os
from matplotlib import pyplot as plt

ruta = os.getcwd() # ruta actual de directorio, puedes cambiar os.getcwd() por una ruta es especial
contenido = os.listdir(ruta) # listado de archivos

# en images se guardaran los nombres de los archivos que terminen con jpg (las imagenes), sin el ".jpg"
images = [x[0:len(x)-4] for x in contenido if x[len(x)-3:len(x)] == 'jpg'] 

# en contenido se esta guardando los archivos que teminen con jpg (guarda las imagenes)
contenido = [cv2.imread(x,1) for x in contenido if x[len(x)-3:len(x)] == 'jpg']

for i in range(len(images)):
	plt.subplot(2, 2, i+1) # subplot(row, column, index)

	real = cv2.flip(contenido[i],1) # voltear horizontalmente la imagen
	cv2.imwrite(images[i]+'_volteado.jpg', real) # guardar esas imagenes con su nombre mas '_volteado"

	# se cambia de BGR a RGB para que se muestre bien en matplotlib, pero nop afecta en como se guarda
	real = cv2.cvtColor(contenido[i], cv2.COLOR_BGR2RGB) 
	plt.imshow(real)
	plt.title(images[i])
	plt.xticks([]), plt.yticks([]) # change de x and y coordinates

plt.show()

cv2.waitKey(0)
	
cv2.destroyAllWindows()