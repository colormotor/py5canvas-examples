from py5canvas import *

img = load_image('../wave-128.png')

def setup():
    size(128, 128)
    no_loop()

def draw():
    image(img, (0, 0))

    img2 = img.resize((64, 64))
    image(img2, (0, 0))

if __name__ == '__main__':
    run()
