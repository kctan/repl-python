import os
from PIL import Image, ImageFilter, ImageOps

filename = "img/clungup.jpg"

im = Image.open(filename)

# ROTATING
#out = im.transpose(Image.ROTATE_90)
#out = im.transpose(Image.ROTATE_180)
#out = im.transpose(Image.ROTATE_270)

# FLIPPING
#out = im.transpose(Image.FLIP_LEFT_RIGHT)
out = im.transpose(Image.FLIP_TOP_BOTTOM)


#im.show()
out.show()
