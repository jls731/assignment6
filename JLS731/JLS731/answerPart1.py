'''
Created by Joseph Song (JLS731)
Assignment #6
Description: This is the function to answer question #1.

Write a modle that creates the 2-D array and then
a) Generate a new array containing the 2nd and 4th rows
b) Generate a new array that contains the 2nd column
c) Generate a new array that contains all the elements in the rectangular section
   between the coordinates [1,0] and [3,2]
d) Generate a new array that contains only elements with values that are between 3
   and 11
   
Print each arrray
'''

import numpy as np

def answerPart1():
    '''Answers Question #1 '''
    NewArray = (np.arange(15).reshape((3,5))+1).transpose()
    return NewArray


def answerPart1a():
    '''Generate a new array containing the 2nd and 4th rows'''
    AnswerArray1a = answerPart1()[[1,3],:]
    return AnswerArray1a

def answerPart1b():
    '''Generate a new array that contains the 2nd column'''
    AnswerArray1b = answerPart1()[:,1]
    return AnswerArray1b

def answerPart1c():
    '''Generate a new array that contains all the elements
        in the rectangular section between the coordinates [1,0] and [3,2]'''
    AnswerArray1c = answerPart1()[1:4,:]
    return AnswerArray1c

def answerPart1d():
    '''Generate a new array that contains only elements with values that 
       are between 3 and 11'''
    AnswerArray1d = answerPart1()[np.logical_and(answerPart1() > 3, answerPart1() < 11)]
    return AnswerArray1d

