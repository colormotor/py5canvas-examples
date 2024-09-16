from py5canvas import *
w = 10

# An array of 0s and 1s
cells = None

# We arbitrarily start with just the middle cell having a state of "1"
generation = 0

# An array to store the ruleset, for example {0,1,1,0,1,1,0,1}
ruleset = [0, 1, 0, 1, 1, 0, 1, 0]

def setup():
    global cells
    create_canvas(640, 400)
    cells = [0] * int(floor(width / w))
    for i in range(len(cells)):
        cells[i] = 0
    cells[floor(len(cells) / 2)] = 1

def draw():
    global cells, generation
    for i in range(len(cells)):
        if cells[i] == 1:
            fill(200)
        else:
            fill(51)
            no_stroke()
            rect(i * w, generation * w, w, w)
    if generation < height / w:
        generate()

# The process of creating the new generation
def generate():
    global cells, generation
    # First we create an empty array for the new values
    nextgen = [0] * len(cells)
    # For every spot, determine new state by examing current state, and neighbor states
    # Ignore edges that only have one neighor
    for i in range(1, len(cells)-1):
        left = cells[i-1]   # Left neighbor state
        me = cells[i]        # Current state
        right = cells[i+1]  # Right neighbor state
        nextgen[i] = rules(left, me, right) # Compute next generation state based on ruleset
    # The current generation is the new generation
    cells = nextgen
    generation += 1

# Implementing the Wolfram rules
# Could be improved and made more concise, but here we can explicitly see what is going on for each case
def rules(a, b, c):
    if a == 1 and b == 1 and c == 1: return ruleset[0]
    if a == 1 and b == 1 and c == 0: return ruleset[1]
    if a == 1 and b == 0 and c == 1: return ruleset[2]
    if a == 1 and b == 0 and c == 0: return ruleset[3]
    if a == 0 and b == 1 and c == 1: return ruleset[4]
    if a == 0 and b == 1 and c == 0: return ruleset[5]
    if a == 0 and b == 0 and c == 1: return ruleset[6]
    if a == 0 and b == 0 and c == 0: return ruleset[7]
    return 0

run()