'''
Created by Joseph Song (JLS731)
Assignment #6
Description: This is the function to answer question #3.

Write a module to generate a 10x3 array of random numbers in the range [0,1].
a. For each row, pick the number closest to 0.5
b. Use abs and argsort to find the column for each of the numbers closest to 0.5
c. Use fancy indexing to extract the numbers into an array

The program should print out a 1-D array containing 10 values, each value is the number
closest to 0.5 from the corresponding row of the original array
'''

import numpy as np

def answerPart3():
    '''This function answers Question 3 '''
    RandomArray = np.random.rand(10,3)
    RandomArrayLessHalf = np.abs(RandomArray - 0.5)
    ColOrder = np.argsort(RandomArrayLessHalf, axis=1)
    
    'Create the col and row indexes for fancy indexing'
    ColIndex = ColOrder[:,0]
    RowIndex = np.arange(10)
    
    AnswerArray3 = RandomArray[RowIndex, ColIndex]
    return AnswerArray3
