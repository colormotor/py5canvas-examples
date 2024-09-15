from py5canvas import *

img1 = load_image('../raspberries-256.jpg')
img2 = load_image('../raspberries-256.jpg')

def setup():
    size(2 * img1.height, img1.height)
    no_loop()

def draw():
    
    img2 = img2.convert('L')
    image(img1, (0, 0))
    image(img2, (width / 2, 0))

if __name__ == '__main__':
    run()
