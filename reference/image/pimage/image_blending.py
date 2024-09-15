from py5canvas import *

img1 = load_image('../src/luminale-512.jpg')
img2 = load_image('../src/grand-theatre-512.jpg')
img3 = load_image('../src/luminale-512.jpg')

# We use PIL.ImageChops for blending
img3 = ImageChops.blend(img2, img3, 0.5)
#img3 = ImageChops.add(img2, img3)
#img3 = ImageChops.multiply(img2, img3)
#img3 = ImageChops.screen(img2, img3)
# img3 = ImageChops.darker(img2, img3)

def setup():
    title("Image blending")
    size(img1.width, int(img1.height * 1.5))
    no_loop()

def draw():
    image(img1, (0, 0), (img1.width // 2, img1.height // 2))
    image(img2, (img1.width // 2, 0), (img1.width // 2, img1.height // 2))
    image(img3, (0, img1.height // 2))


run()
