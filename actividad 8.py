import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
plt.rcParams["image.cmap"]="grey"

im1=Image.open("imagen.thonny.jpg")
ar=np.array(im1)

plt.imshow(ar)
plt.show()

filas=315
columnas=474
gris=np.zeros((315,474))

for i in range(filas):
    for j in range(columnas):
        gris[i][j]=ar[i][j][0]*0.2989+ar[i][j][0]*0.5870+ar[i][j][0]*0.1140
        
plt.imshow(gris, cmap="grey")
plt.show()