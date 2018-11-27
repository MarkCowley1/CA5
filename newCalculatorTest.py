# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:39:27 2018

@author: hp
"""

import unittest #import unittest and below import all functions from our file, newCalculator.
from newCalculator import *

class CalculatorTest(unittest.TestCase):
    
    def testAdd(self):#Make sure all functions run normally through ASsertEqual testing
        self.assertEqual(6, add([2,2,2]))
    def testSubtract(self):
        self.assertEqual(2, subtract(4,2))
    def testMultiply(self):
        self.assertEqual(6, multiply(2,3))
    def testDivision(self):
        self.assertEqual('Division By Zero Not Allowed', division(1,0))
        self.assertEqual(0.5, division(1,2))
    def testSquared(self):
        self.assertEqual(9, squared(3))
    def testCubed(self):
        self.assertEqual(27, cubed(3))
    def testPower(self):
        self.assertEqual(27, power(3,3))
    def testSqrt(self):
        self.assertEqual(5, sqrt(25))
    def testSin(self):
        self.assertEqual(1, sin(90))
    def testCos(self):
        self.assertEqual(0.5000000000000001, cos(60))
    def testTan(self):
        self.assertEqual(1.7320508075688767, tan(60))
    
if __name__ == '__main__':        
    unittest.main() #look through all the code for the word 'test.'
