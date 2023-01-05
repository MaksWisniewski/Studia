"""
Maksymilian Wiśniewski

Langton's ant is a two-dimensional cellular automaton that 
follows a simple set of rules. The ant moves on a grid of 
cells, each of which can be in one of two states: black or 
white. At each step, the ant looks at the color of the cell
it is currently on, and then performs the following actions:

If the cell is white, the ant turns 90 degrees to the right 
and changes the color of the cell to black.

If the cell is black, the ant turns 90 degrees to the left 
and changes the color of the cell to white.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the size of the grid
N = 100

# Create a grid of cells and initialize them to be white
grid = np.ones((N, N))

# Place the ant at the center of the grid, facing up
x, y = N // 2, N // 2
direction = 0  # 0: up, 1: right, 2: down, 3: left

# Implement the update function for the animation
def update(num):
    global x, y, direction
    
    # Get the color of the current cell
    cell_color = grid[x, y]
    
    # Update the direction and color of the cell based on the rules of Langton's ant
    if cell_color == 1:  # White cell
        direction = (direction + 1) % 4
        grid[x, y] = 0
    else:  # Black cell
        direction = (direction - 1) % 4
        grid[x, y] = 1
    
    # Update the position of the ant based on the direction it is facing
    if direction == 0:  # Ant is facing up
        x -= 1
    elif direction == 1:  # Ant is facing right
        y += 1
    elif direction == 2:  # Ant is facing down
        x += 1
    elif direction == 3:  # Ant is facing left
        y -= 1
    
    # Wrap the ant's position around the edges of the grid if it goes off the grid
    x = x % N
    y = y % N
    
    # Update the plot with the new grid and ant position
    im.set_array(grid)
    line.set_data([x], [y])
    return im, line

# Set up the plot
fig, ax = plt.subplots()
im = ax.imshow(grid, cmap='binary')
line, = ax.plot([x], [y], 'ro')

# Create the animation using the update function
ani = animation.FuncAnimation(fig, update, frames=range(1000), interval=10, blit=True)

# Show the plot
plt.show()