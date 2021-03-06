"""
Conway's Game of Life
Any live cell with fewer than two live neighbours dies, as if caused by under-population.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overcrowding.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""
import time
import random
import sys

DIRECTIONS = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1, 1), (-1,0)]

def game_loop(grid, max_turns=1000, turn_delay=0.8):
    """
    grid: array of arrays, a single value is grid[y][x]
    """
    for count in xrange(max_turns):
        display(grid)
        grid, has_live = turn(grid)
        if not has_live:
            break
        time.sleep(turn_delay)

def turn(grid):
    next = create_grid(len(grid[0]), len(grid))
    has_live = False
    for y in xrange(len(grid)):
        for x in xrange(len(grid[0])):
            count = neighbors(y, x, grid)
            if ((grid[y][x] and 2 <= count <= 3)
                or (not grid[y][x] and count == 3)):
                next[y][x] = 1
                has_live = True
    return next, has_live

def neighbors(y, x, grid):
    ymax = len(grid) - 1
    xmax = len(grid[0]) - 1
    count = 0
    for dy, dx in DIRECTIONS:
        ny, nx = y + dy, x + dx
        ny = wrap(ny, ymax)
        nx = wrap(nx, xmax)
        if grid[ny][nx]:
            count += 1
    return count

def wrap(y, max):
    if y < 0:
        y = max
    elif y > max:
        y = 0
    return y

def create_grid(width, height):
    grid = []
    for y in xrange(height):
        grid.append([0,]*width)
    return grid

def display(grid):
    print '_'*len(grid[0]) + 'v'

    for y in xrange(len(grid)):
        for x in xrange(len(grid[y])):
            c = ' '
            if grid[y][x]:
                c = '*'
            sys.stdout.write(c)

        print
    print '_'*len(grid[0]) + '^'

def seed(grid, coords):
    for y,x in coords:
        grid[y][x] = 1

def _random_coords(quantity, height, width):
    coords = []
    for x in xrange(quantity):
        coords.append((random.randint(0, height-1), random.randint(0, width-1)))
    return coords

def test_all():
    height = 30
    width = 30
    grid = create_grid(height, width)
    seed(grid, _random_coords(130, height, width))
    #seed(grid, [(10,10), (11,10), (12,10), (8,8), (25,23), (24,23), (3,3), (3,4), (4,3), (20,3), (20,4), (23,3), (23,4), (5,13), (6,13), (6, 14)])
    game_loop(grid)

if __name__ == '__main__':
    test_all()

