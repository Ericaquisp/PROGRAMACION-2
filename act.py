import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps
plt.rcParams['image.cmap'] = 'gray'

im1=Image.open("imagen.thonny.jpg")
im1gr=ImageOps.grayscale(im1)
ar = np.array(im1gr)

plt.imshow(ar)
plt.show()

filas=315
columnas=474
aux=0
ind_op=0
 
for i in range(filas):
    for j in range (int (columnas/2)):
        ind_op=columnas-1-j
        aux=ar[i][j]
        ar[i][j]=ar[i][ind_op]
        ar[i][ind_op]=aux

plt.imshow(ar)
plt.show()
        
