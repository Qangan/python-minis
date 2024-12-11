import numpy as np
import time

def timing_val(func):
    def wrapper(*arg, **kw):
        '''source: http://www.daniweb.com/code/snippet368.html'''
        t1 = time.time()
        res = func(*arg, **kw)
        t2 = time.time()
        print(f"{arg[0].__name__} took {(t2 - t1) * 1000} ms")
        return
    return wrapper

@timing_val
def timeit(func):
  for i in range(128):
    func()
  return

def nextGeneration():
    
    global grid

    future = [[0 for i in range(128)] for j in range(128)]
    
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

    grid = future


def nextGenerationNP():
    
    global gridnp

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

    gridnp = np.copy(future)

gridnp = np.zeros((128,128))

gridnp[13][15] = 1
gridnp[15][15] = 1
gridnp[15][14] = 1
gridnp[15][16] = 1

gridnp[14][10] = 1
gridnp[15][10] = 1
gridnp[14][9] = 1

grid = [[0 for i in range(128)] for j in range(128)]

grid[13][15] = 1
grid[15][15] = 1
grid[15][14] = 1
grid[15][16] = 1

grid[14][10] = 1
grid[15][10] = 1
grid[14][9] = 1

timeit(nextGenerationNP)
timeit(nextGeneration)
