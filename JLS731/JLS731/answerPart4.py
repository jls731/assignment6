'''
Created by Joseph Song (JLS731)
Assignment #6
Description: This is the function to answer question #4.

Write a module that computes the Mandelbrot fractal using the Mandelbrot interation

'''

import numpy as np
import matplotlib.pyplot as plt

def answerPart4():
    ''' This functions answers question #4 '''
    N_max = 50
    some_threshold = 50  
    
    'Create the x, y span'
    xspan = np.arange(-2, 1, 0.005)
    yspan = np.arange(-1.5, 1.5, 0.005)
    
    'Grab the size of the span'
    xsize = xspan.size
    ysize = yspan.size
    
    'Create 2d boolean grid'
    mask = np.ones((xsize, ysize), dtype=bool)
    
    for x in range(xsize):
        for y in range(ysize):
            c = xspan[x] + 1j*yspan[y]
            z = c
            for v in range(N_max):
                z = z**2 + c
                if abs(z) >= some_threshold:
                    mask[x,y] = False
                    break
                    
    plt.imshow(mask.T, extent=[-2,1,-1.5,1.5])
    plt.gray()
    return plt.savefig('mandelbrot.png')