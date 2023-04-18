'''
   CS5001
   Fall 2022
   Elif Tirkes 
   Homework 7: Simple Fraction Class
'''

class SimpleFraction():
    '''
    Class -- SimpleFraction 
        Creates an int fraction with a numerator and a denominator.
        Can also accomodate for scalars (i.e. 1 will turn into 1/1).
        includes get_numerator(), which returns the numerator of the
        fraction, get_denominator() which returns the denominator of
        the fraction, make_reciprocal() which flips the placement
        of the numerator and denominator in a new variable
        and returns it, validate() which checks if the numerator
        and denominator value are ints, otherwise returns a ValueError,
        multiply() which multiplies the fraction with another, divide()
        which divides the fraction with another, and __str__() which
        returns the value of the fraction and __eq__() which checks
        if two fractions of this class are the same.  
    '''
    
    def __init__(self, numerator=1, denominator=1):
        '''
        Function -- __init__
            constructor for SimpleFraction() which inputs
            a denominator, numerator, and validates the fraction
            value. Default value for both is 1/1. 
        Parameters:
            self -- current SimpleFraction() object
            numerator -- int, default 1 unless stated otherwise
            denominator -- int, default 1 unless stated otherwise
        '''
        if type(numerator) == int:
            self.numerator = numerator
        else:
            raise ValueError
        
        if type(denominator) == int:
            self.denominator = denominator
        else:
            raise ValueError 

    def get_numerator(self):
        '''
        Function -- get_numerator
            returns the current numerator
            value of the function
        Parameters:
            self -- current SimpleFraction() object
            with numerator attribute
        Returns numerator int value
        '''
        return self.numerator
    
    def get_denominator(self):
        '''
        Function -- get_denominator
            returns the current denominator
            value of the function
        Parameters:
            self -- current SimpleFraction() object
            with denominator attribute
        Returns denominator int value
        '''
        return self.denominator
    
    def make_reciprocal(self):
        '''
        Function -- make_reciprocal
            Creates a new value, calls SimpleFraction with the
            denominator and numerator flipped to get the reciprocal
            of the self object fraction 
        Parameters:
            self -- current SimpleFraction() object

        Returns variable called reciprocal with flipped numerator and
        denominator 
        '''
        reciprocal = SimpleFraction(self.get_denominator(),
                                    self.get_numerator())
        if not reciprocal.validate() == ValueError: 
            return reciprocal
            
    def validate(self):
        '''
        Function -- validate
            validates that the self object is a fraction by
            using isinstance() to see if the numerator and
            denominator is type int. Raises ValueError
            otherwise. 
        Parameters:
            self -- current SimpleFraction() object
        '''
        if not (isinstance(self.get_numerator(), int) and
                isinstance(self.get_denominator(), int)):
            # checks to see if the numerator and denominator are integers 
            raise ValueError
    
    def multiply(self, other):
        '''
        Function -- multiply
        if the other object is in the class SimpleFraction, multiplies the
        numerators and denominators together. If the other object is
        not a fraction (scalar), multiplies the numerator of the
        self object with the scalar to accurately multiply a fraction
        with a non-fraction input.
        Parameters:
        self -- current SimpleFraction() object
        other -- another instance / input in the SimpleFraction() class

        Returns variable called
        fraction_multiply with the multiplied fraction values
        '''
        if isinstance(other, SimpleFraction):
            # if other object is in the class
            # / type SimpleFraction (if it's a fraction)
            fraction_multiply = SimpleFraction(self.get_numerator() *
                                               other.get_numerator(),
                                               self.get_denominator() *
                                               other.get_denominator())
        else:
            # for scalars since bottom is 1,
            # only multiplies the numerator
            # and returns the same denominator as the self 
            fraction_multiply = SimpleFraction(self.get_numerator() *
                                               other, self.get_denominator())
        return fraction_multiply
    
    def divide(self, other):
        '''
        Function -- divide
            if the other object is in the class SimpleFraction, multiplies the
            numerators and denominators together after making a reciprocal
            of the other object. If the other object is
            not a fraction (scalar), multiplies the denominator of the
            self object with the scalar to accurately multiply a fraction
            with a non-fraction input.
        Parameters:
            self -- current SimpleFraction() object
            other -- another instance / input in
            the SimpleFraction() class

            Returns variable called fraction_divide
            with the divided fraction values
        '''
        if isinstance(other, SimpleFraction):
            # if other object is in the class /
            # type SimpleFraction (if it's a fraction)
            fraction_divide = self.multiply(other.make_reciprocal())
            return fraction_divide 
            # uses the multiply function on self and takes in a
            # flipped version of other
            #  using the make_reciprocal function 
        else:
            fraction_divide = SimpleFraction(self.get_numerator(),
                                             self.get_denominator() * other)
            return fraction_divide
            # if number is a scalar, multiplies denominator with the fraction
            # as both numerator and denominator are the same
          
    def __str__(self):
        '''
        Function -- ___str__
            Prints a string with the numerator and denominator of the
            SimpleFraction() class object 
        Parameters:
            self -- current SimpleFraction() object
            other -- another instance / input in the SimpleFraction() class
        '''
        return f"{self.get_numerator()}/{self.get_denominator()}"
        # prints the fraction 
    
    def __eq__(self, other):
        '''
        Function -- __eq__
            divides the self object with the other object,
            if the fractions are the same then the numerator and
            denominator will be the same int value. Returns
            a boolean value indicating whether the numerator and
            denominator are the same value. 
        Parameters:
            self -- current SimpleFraction() object
            other -- another instance / input in the SimpleFraction() class

        Returns a bool value indicating whether the numerator and
        denominator are the same
        '''
        frac_equals = self.divide(other)
        # if the fractions are the same, then
        # the denominator and numerator will be the same
        # when they are flipped and multiplied
        # i.e. 1/2 * 1/2 = 2/2
        check = frac_equals.get_denominator() == \
            frac_equals.get_numerator()
        return check
        # returns true or false depending on whether
        # the denominator and numerator are the same 
