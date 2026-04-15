import imageio.v3 as iio
from PIL import Image
import numpy as np

files = ['camera-1.png' , 'camera-2.png']
cameras = [ ]

size = (400,400)

for file in files:
  img = Image.open(file)
  img = img.resize(size)
  cameras.append(np.array(img))

iio.imwrite('camer-click1.gif' , cameras , duration=500 , loop=0)