# A simple snake game
#
# Controls:
#   - Arrow keys start the game and control the snake.
#   - Spacebar pauses the game.

from py5canvas import *

tiles = 25
tile_size = 25
background_color = Color(24)
pause_overlay_color = Color(88, 127)

paused = False

head = Vector(tiles // 2, tiles // 2)
velocity = Vector(0, 0)
tail = []
tail_size = 5
snake_color = Color(161, 181, 108)

food = Vector(int(random_uniform(tiles)), int(random_uniform(tiles)))
food_color = Color(171, 70, 66)

def setup():
    size(tile_size * tiles, tile_size * tiles)
    title("p5 Snake")

    no_stroke()

def draw():
    global head
    global tail
    global tail_size
    global paused

    # Stop right here if the game is paused
    if paused:
        return

    background(background_color)

    fill(snake_color)
    for cell in tail:
        square(cell * tile_size, 0.8 * tile_size)

    head = head + velocity
    if head[0] < 0:
        head[0] = tiles - 1
    if head[0] > tiles - 1:
        head[0] = 0

    if head[1] < 0:
        head[1] = tiles - 1
    if head[1] > tiles - 1:
        head[1] = 0

    # Pause and reset the game when the snake eats itself.
    for pos in tail:
        if dist(pos, head) < 0.1:
            tail_size = 5
            tail = []
            paused = True

            fill(lerp(food_color, snake_color, 0.7))
            square(head * tile_size, 0.8 * tile_size)

    tail.append(head)
    if len(tail) > tail_size:
        extra_cells = len(tail) - tail_size
        tail = tail[extra_cells:]

    if dist(head, food) < 0.1:
        fill(lerp(food_color, snake_color, 0.3))
        square(head * tile_size, 0.8 * tile_size)
        food[0] = floor(random_uniform(0, tiles))
        food[1] = floor(random_uniform(0, tiles))
        tail_size += 1

    fill(food_color)
    square(food * tile_size, 0.8 * tile_size)

    if paused:
        background(pause_overlay_color)

def key_pressed(key):
    global paused
    global velocity

    if key in ['UP', 'DOWN', 'RIGHT', 'LEFT', 'h', 'j', 'k', 'l']:
        paused = False
        if key == 'UP' or key == 'k':
            velocity[0] = 0
            velocity[1] = -1
        elif key == 'DOWN' or key == 'j':
            velocity[0] = 0
            velocity[1] = 1
        elif key == 'RIGHT' or key == 'l':
            velocity[0] = 1
            velocity[1] = 0
        elif key == 'LEFT' or key == 'h':
            velocity[0] = -1
            velocity[1] = 0
    elif key == ' ':
        paused = not paused
        if paused:
            # Hide the food before drawing the overlay.
            fill(background_color)
            square(food * tile_size, 0.8 * tile_size)
            background(pause_overlay_color)

if __name__ == '__main__':
    run(frame_rate=15)
