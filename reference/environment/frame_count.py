from py5canvas import *

def draw():
    background(204)
    line((0, 0), (width, height))
    print(frame_count)

run(frame_rate=30)
