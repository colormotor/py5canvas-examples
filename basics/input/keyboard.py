from py5canvas import *

key=''

def setup():
    size(512, 512)
    frame_rate(60)

def draw():
    background(0)
    fill(255)
    text_size(120)
    if key:
        text(key, width/2, height/2, align='center', valign='center')

def key_pressed(k):
    global key
    key = k
    print('pressed:', k)

run()

