#
# Constrain
#
# Move the mouse across the screen to move the circle. THe program
# constrains the circle to its box.
from py5canvas import *

easing = 0.05
radius = 24
edge = 100
inner = edge + radius
m = Vector(0, 0)

def setup():
    size(640, 360)
    title("Constrain")
    no_stroke()
    ellipse_mode('RADIUS')
    rect_mode('CORNERS')

def draw():
    background(51)

    if abs(mouse_x - m[0]) > 0.1:
        m[0] = m[0] + (mouse_x - m[0]) * easing

    if abs(mouse_y - m[1]) > 0.1:
        m[1] = m[1] + (mouse_y - m[1]) * easing

    m[0] = constrain(m[0], inner, width - inner)
    m[1] = constrain(m[1], inner, height - inner)

    fill(76)
    rect((edge, edge), (width - edge, height - edge))

    fill(255)
    circle(m, radius)

if __name__ == '__main__':
    run()
