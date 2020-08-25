from PIL import Image
import glob
from os import path

types = ('*.png', '*.jpg', '*.jpeg', '*.wai', '*.tmp', '*tif')
images = []

for tp in types:
    images.extend(glob.glob(tp))

for image in images:
	im = Image.open(image)
	end = path.splitext(im.filename)[1]
	if(not end == ".jpg"):
		beg = path.splitext(im.filename)[0]
		im.save('./png/{0}.jpg'.format(beg))
