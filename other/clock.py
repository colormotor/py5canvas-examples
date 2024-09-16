from py5canvas import *
from datetime import datetime

def setup():
    create_canvas(400, 400)

def draw():
    time = datetime.now()

    background(0)
    translate(200, 200)
    rotate_deg(-90)

    hr = time.hour
    mn = time.minute
    sc = time.second

    stroke_weight(8)
    stroke(255, 100, 150)
    no_fill()
    second_angle = map(sc, 0, 60, 0, 360)
    arc(0, 0, 300, 300, 0, second_angle)

    stroke(150, 100, 255)
    minute_angle = map(mn, 0, 60, 0, 360)
    arc(0, 0, 280, 280, 0, minute_angle)

    stroke(150, 255, 100)
    hour_angle = map(hr % 12, 0, 12, 0, 360)
    arc(0, 0, 260, 260, 0, hour_angle)

    push()
    rotate_deg(second_angle)
    stroke(255, 100, 150)
    line(0, 0, 100, 0)
    pop()

    push()
    rotate_deg(minute_angle)
    stroke(150, 100, 255)
    line(0, 0, 75, 0)
    pop()

    push()
    rotate_deg(hour_angle)
    stroke(150, 255, 100)
    line(0, 0, 50, 0)
    pop()

    stroke(255)
    #point(0, 0)

    push()
    rotate_deg(90)
    fill(255)
    no_stroke()
    pop()

run()