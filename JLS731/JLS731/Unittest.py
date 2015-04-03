'''
Created by Joseph Song (JLS731)
Assignment #6
Description: This is the unittest to test the first three modules to make sure
produces the correct outputs. I do not test anything for part 4 since it produces
a file.

'''
import unittest
import numpy as np

from answerPart1 import *
from answerPart2 import *
from answerPart3 import *


class Test(unittest.TestCase):


    def testPart1(self):
        '''Checks shape and accuracy of the output'''
        
        self.correctAnswer1 = np.array([[1,6,11], [2,7,12], [3,8,13], [4,9,14],[5,10,15]])
        self.correctAnswer1a = np.array([[2,7,12],[4,9,14]])
        self.correctAnswer1b = np.array([6,7,8,9,10])
        self.correctAnswer1c = np.array([[2,7,12],[3,8,13],[4,9,14]])
        self.correctAnswer1d = np.array([6,7,8,4,9,5,10])
        
        self.assertTrue((answerPart1()==self.correctAnswer1).all(), "Incorrect values")
        self.assertTrue((answerPart1a()==self.correctAnswer1a).all(), "Incorrect values")
        self.assertTrue((answerPart1b()==self.correctAnswer1b).all(), "Incorrect values")
        self.assertTrue((answerPart1c()==self.correctAnswer1c).all(), "Incorrect values")
        self.assertTrue((answerPart1d()==self.correctAnswer1d).all(), "Incorrect values")
        self.assertEqual(answerPart1().shape, (5,3), "The shape of initial array is incorrect")
        self.assertEqual(answerPart1a().shape, (2,3), "The shape of the array is incorrect")
        self.assertEqual(answerPart1b().shape, (5,), "The shape of the array is incorrect")
        self.assertEqual(answerPart1c().shape, (3,3), "The shape of the array is incorrect")
        self.assertEqual(answerPart1d().shape, (7,), "The shape of the array is incorrect")


    def testPart2(self):
        '''Checks shape of the output'''
        self.assertEqual(answerPart2().shape, (5,5), "The shape of the array is incorrect")
    def testPart3(self):
        '''Checks shape of the output'''
        self.assertEqual(answerPart3().shape, (10,), "The shape of the array is incorrect")
        



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()