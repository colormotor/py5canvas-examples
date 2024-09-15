from py5canvas import *
import pdb

img = load_image('../raspberries-256.jpg')

def setup():
    size(2 * img.height, img.height)
    no_loop()

def draw():
    blurred = img.filter(ImageFilter.GaussianBlur(2.0))
    
    image(img, (0, 0))
    image(blurred, (width / 2, 0))

run()