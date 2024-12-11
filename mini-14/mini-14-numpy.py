import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import numpy as np

def nextGeneration(data):
    
    global grid

    future = np.zeros((128, 128))
    
    for l in range(128):
        for m in range(128):
            aliveNeighbours = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    if ((l+i>=0 and l+i<128) and (m+j>=0 and m+j<128)):
                        aliveNeighbours += grid[l + i][m + j]

            aliveNeighbours -= grid[l][m]

            if ((grid[l][m] == 1) and (aliveNeighbours < 2)):
                future[l][m] = 0

            elif ((grid[l][m] == 1) and (aliveNeighbours > 3)):
                future[l][m] = 0

            elif ((grid[l][m] == 0) and (aliveNeighbours == 3)):
                future[l][m] = 1
            else:
                future[l][m] = grid[l][m]

    grid = np.copy(future)
    mat.set_data(grid)
    return [mat]


grid = np.zeros((128,128))

grid[13][15] = 1
grid[15][15] = 1
grid[15][14] = 1
grid[15][16] = 1

grid[14][10] = 1
grid[15][10] = 1
grid[14][9] = 1

fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, nextGeneration, interval=25, save_count=50, frames = range(128))

plt.show()

