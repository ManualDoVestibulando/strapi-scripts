from PIL import Image
import numpy as np

image = Image.open('./teste.jpg')
imarr = np.array(image)
print( float(imarr.shape[0])/float(imarr.shape[1]) )

cropped = imarr[ 250:imarr.shape[0], :imarr.shape[1] ]
nimg = Image.fromarray(cropped)

Image._show(nimg)
