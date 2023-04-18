'''
   CS5001
   Fall 2022
   Elif Tirkes
   Homework 2: Programming #1- Temperature Converter Code Tester
'''

from temperature_conversion import convert_fahrenheit_to_celsius
from temperature_conversion import convert_celsius_to_fahrenheit

def test_conversion_to_fahrenheit(temperature, expected_conversion):
    '''
        Function -- input an expected conversion from celsius to
        fahrenheit, calls for another function to make an actual conversion,
        and prints both the expected and actual conversion
        Parameters:
            temperature (float) - the original temperature that will be converted
            expected_conversion - the expected conversion from celsius to fahrenheit
        Prints the initial temperature without conversion, the expected conversion as a float,
        and the actual conversion from the imported convert_fahrenheit_to_celsius function 
    '''
    print("Converting", temperature, "F to Celsius --")
    print(f"Expected result = {expected_conversion}", "Celsius")
    actual = convert_fahrenheit_to_celsius(temperature)
    print(f"Actual result = {actual:.2f}", "Celsius")
    #prints actual conversion to two decimal places 

def test_conversion_to_celsius(temperature, expected_conversion):
    '''
        Function -- input an expected conversion from fahrenheit to
        celsius, calls for another function to make an actual conversion,
        and prints both the expected and actual conversion
        Parameters:
            temperature (float) - the original temperature that will be converted
            expected_conversion - the expected conversion from fahrenheit to celsius
        Prints the initial temperature without conversion, the expected conversion as a float,
        and the actual conversion from the imported convert_fahrenheit_to_fahrenheit function 
    '''
    print("Converting", temperature, "C to Fahrenheit --")
    print(f"Expected result = {expected_conversion}", "Fahrenheit")
    actual = convert_celsius_to_fahrenheit(temperature)
    print(f"Actual result = {actual:.2f}", "Fahrenheit")
    #prints actual conversion to two decimal places 

def main():

    temperature_type= str(input("Are you converting Celsius or Fahrenheit? (C/F)"))
        #Asks the user whether the initial temperature is celsius or in fahrenheit 

    temperature = float(input("What temperature are you converting? (Please input numbers only)"))
        #Asks the user what the temperature value is, inputs a float

    if temperature_type.upper() == "C":
        expected_conversion = float(input("What is your expected Fahrenheit conversion to Celsius?"))
        test_conversion_to_fahrenheit(temperature,expected_conversion)
        #checks if the user is trying to convert fahrenheit to c,
        #and directs to the appropriate function 
    
    elif temperature_type.upper() == "F":
        expected_conversion = float(input("What is your expected Celsius conversion to Fahrenheit?"))
        test_conversion_to_celsius(temperature, expected_conversion)
        #checks if the user if converting from fahrenheit to celsius instead
        #and directs user to appropriate function 
      
    else:
        print("Error with input. Please input only valid numbers")
        #if either the temperature input or the temperature type input is wrong,
        #prompts the user to run the function with better inputs 
        


if __name__ == "__main__":
   main()
