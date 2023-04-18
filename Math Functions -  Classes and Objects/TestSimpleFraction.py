'''
   CS5001
   Fall 2022
   Elif Tirkes 
   Homework 7: Test Simple Fraction
'''

# from SimpleFraction.py import SimpleFraction
import unittest

class SimpleFractionTest(unittest.TestCase):
    fraction_example = SimpleFraction(1,8)
    # input an example simple fraction, 1/8
    default_example = SimpleFraction()
    # input nothing, default 1/1

    def testConstructor(self):
        '''
        Function -- testConstructor
            Tests if the constructor inputs and
            outputs the int values as strings
            correctly using unittest. 
        Parameters:
            self -- current SimpleFraction() object
        '''
        # tests if constructor inputs
        # and returns strings of the inputs correctly 
        self.assertEqual(str(self.fraction_example), "1/8")
        self.assertEqual(str(self.default_example), "1/1")
    
    def testMultiply(self):
        '''
        Function -- testMultiply
            Tests if the multiply() function works correctly in
            SimpleFraction() by comparing expected values with
            test values. 
        Parameters:
            self -- current SimpleFraction() object
        '''
        # tests the multiply function 
        mult_self = self.fraction_example.multiply(self.fraction_example)
        # multiply fraction with self
        self.assertEqual(str(mult_self), "1/64")
        self.assertEqual(str(self.fraction_example.multiply(2)), "2/8")
    
    def testDivide(self):
        '''
        Function -- testDivide
            Tests if the divide() function works correctly in
            SimpleFraction() by comparing expected values with
            test values. 
        Parameters:
            self -- current SimpleFraction() object
        '''
        # tests the divide function
        self.assertEqual(str(self.fraction_example.divide(self.fraction_example)), "8/8")
        self.assertEqual(str(self.fraction_example.divide(2)), "1/16")
    
    def testEq(self):
        '''
        Function -- testEq
            Tests if the __eq__() function works correctly by
            checking if the function returns a True when the
            numerator and denominator are the same, and False
            when otherwise. 
        Parameters:
            self -- current SimpleFraction() object
        '''
        # tests the function that checks sameness
        self.assertEqual(self.fraction_example == self.fraction_example, True)
        self.assertEqual(self.fraction_example == self.default_example, False)
