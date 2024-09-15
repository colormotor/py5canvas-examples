from py5canvas import *

# Copy an image by considering it a numpy array
# This will enable "slicing" but disable PIL functionalities
raspberries = np.array(load_image("../raspberries-256.jpg"))

def setup():
    size(*raspberries.shape[:2])

    raspberries[:128, :] = raspberries[128:, :]
    no_loop()

def draw():
    image(raspberries)

if __name__ == '__main__':
    run()
