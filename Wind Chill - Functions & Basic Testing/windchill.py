'''
   CS5001
   Fall 2022
   Elif Tirkes 
   Homework 2: Temperature Converter Using Metric Wind Chill Index 
'''

from temperature_conversion import convert_fahrenheit_to_celsius
from temperature_conversion import convert_celsius_to_fahrenheit

def convert_mph_to_kmph(x: float) -> float:
    '''
    Function -- convert_mph_to_kmph
        Converts speed from mph to kmph
    Parameters:
        x (float) -- the original wind speed in miles per hour
    Returns a float value representing the converted wind speed
    in kilometers per hour
    '''
    
    MPH_CONVERSION_FACTOR = 1.61
    x = x * MPH_CONVERSION_FACTOR
    return x

def calculate_windchill(air_temp_fahrenheit, wind_speed_in_miles):
    '''
    Function -- calculate_windchill
        calculates adjusted temperature based on wind chill.
        Calls for convert_mph_to_kmph function to convert wind speed
         into metric units, then calls for convert_fahrenheit_to_celsius
         function to convert the temperature to celsius
         in order to input into the metric equation.
         Calls for convert_celsius_to_fahrenheit function after calculating
         windchill to convert result back into imperial units. 
    Parameters:
        air_temp_fahrenheit -- inputs the air temperature in
        imperial units, converts it into metric
        wind_speed_in_miles -- inputs wind speed in imperial
        units, converts it into metric 
    Returns a float value representing the windchill in imperial units.
    '''
    
    # convert wind speed from metric to imperial using mph_to_kmph function 
    wind_speed_in_kmph = float(convert_mph_to_kmph(wind_speed_in_miles))

    # convert temperature from metric to imperial units using imported function 
    air_temp_celsius = float(convert_fahrenheit_to_celsius(air_temp_fahrenheit))

    # calculate windchill using index equation (metric units) 
    windchill_index = (13.12 + 0.6215 * air_temp_celsius - 11.37 * (wind_speed_in_kmph ** 0.16) + 0.3965 * air_temp_celsius * (wind_speed_in_kmph ** 0.16))

    # convert windchill temperature back to fahrenheit using imported function 
    windchill_fahrenheit = convert_celsius_to_fahrenheit(windchill_index)
    
    return windchill_fahrenheit


def main():
    air_temp_fahrenheit = float(input("What is the temperature in Fahrenheit?"))
    # inputs the air temperature in fahrenheit from user 
    wind_speed_in_miles = float(input("What's the wind speed in miles-per-hour?"))
    # inputs the wind speed in miles from user 
    print(f"The temperature based on wind chill is {calculate_windchill(air_temp_fahrenheit , wind_speed_in_miles):.2f} Fahrenheit")


if __name__ == "__main__":
    main()
