import math
import time

x = 0
y = 0
arrayWidth = []
grid = []
counter = 0
visualize = False

print("Welcome to my 2D binary search algorithm implementation")
gridWidth = int(input("Type in the grid width, it has to be greater than 1: "))
gridHeight = int(input("Type in the grid height, it has to be greater than 0: "))
keyX = int(input("Type in the X coordinate of the Key, it has to be"
                 "bigger than 0, equal to or smaller than the grid width (0<X<=Width): "))
keyY = int(input("Type in the Y coordinate of the Key, it has to be"
                 "bigger than 0, equal to or smaller than the grid height (0<Y<=Height): "))
print('\n')
if 'y' in input('Do you want to visualize the process? only visualize grids smaller than 30x50 (type "y" to yes): '):
    visualize = True
    print('X is the key position, O is the current algorithm position, Θ means that the current position is the same as'
          'the key position')
print(3*'\n')

minX = 0
maxX = gridWidth-1
minY = 0
maxY = gridHeight-1

while counter < gridWidth:      # Creates X axis
    arrayWidth.append([" "])
    counter += 1

counter = 0

while counter < gridHeight:     # Creates Y axis
    grid.append(arrayWidth.copy())
    counter += 1

counter = 0

grid[keyY-1][keyX-1] = ['X']        # Places key
grid[y][x] = ['O']      # Starting point

if visualize:
    for i in grid:
        print(i)

print("\n")

while x != (keyX-1) or y != (keyY-1):
    grid[y][x] = [' ']

    if keyX-1 > x:
        minX = x + 1
        x = math.floor((maxX + minX)/2)

    elif keyX-1 < x:
        maxX = x - 1
        x = math.floor((minX + maxX)/2)

    if keyY-1 > y:
        minY = y + 1
        y = math.floor((maxY + minY)/2)

    elif keyY-1 < y:
        maxY = y - 1
        y = math.floor((minY + maxY)/2)

    if x == keyX-1 and y == keyY-1:
        grid[y][x] = ['Θ']
    else:
        grid[y][x] = ['O']
        counter += 1

    print(f'x:{x+1} y:{y+1}')

    if visualize:
        for i in grid:
            print(i)

    print('\n')

print(f'Hey, i found your key! it is located at ({x+1},{y+1})')
print(f'Took me {counter} rounds to find')

time.sleep(60)


