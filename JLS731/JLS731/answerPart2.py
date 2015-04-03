'''
Created by Joseph Song (JLS731)
Assignment #6
Description: This is the function to answer question #2.

Write a module that, given the array:
a = np.arange(25).reshape(5,5)
divides each column element-wise with the array
b = np.array([1.,5,10,15,20])
'''

import numpy as np

def answerPart2():
    '''Function to answer Part 2'''
    
    a = np.arange(25).reshape(5,5)
    b = np.array([1., 5, 10, 15, 20]).reshape(5,1)
    AnswerArray2 = a/b
    return AnswerArray2
    
    