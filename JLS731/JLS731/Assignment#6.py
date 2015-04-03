'''
Created by Joseph Song (JLS731)
Assignment #6
Description: This is the main program that runs all the different modules 
and prints out the results
'''

from answerPart1 import *
from answerPart2 import *
from answerPart3 import *
from answerPart4 import *

if __name__ == '__main__':
    
    print "Answer to question 1: initial array"
    print answerPart1()
    
    print "Answer to question 1a: new array that contains 2nd and 4th rows"
    print answerPart1a()
    
    print "Answer to question 1b: new array that contains the 2nd column"
    print answerPart1b()
    
    print "Answer to question 1c: all elements in the rectangular section"
    print answerPart1c()
    
    print "Answer to question 1d: array with only elements in (3,11)"
    print answerPart1d()
    
    print "Answer to question 2: Element-wise division result"
    print answerPart2()
    
    print "Answer to question 3: 1D array containing 10 values that are closest to 0.5"
    print answerPart3()
    
    print "Answer to question 4: Saves an mandlebrot plot as a png file"
    print "Calculating..."
    answerPart4()
    print "Finished"
    