from py5canvas import *

img = load_image('../soyuz-256.jpg')

def setup():
    size(*img.size)
    no_loop()

def draw():
    white = Color(255, 255, 255)
    # Convert to array to maniuplate
    pixels = to_array(img)
    for px in range(16, width-1, 16):
        for py in range(16, height-1, 16):
            pixels[py, px] = white
    # We can visualize the pixels directly
    # but to convert them back to an image we could do
    # img2 = to_image(pixels) 
    image(pixels, (0, 0))

if __name__ == '__main__':
    run()
