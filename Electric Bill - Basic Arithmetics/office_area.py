'''
    Elif Tirkes
    CS 5001, Fall 2022
    Homework  1 - Program 3, Area of an Office

    This is a basic program that reads the area of
    an office in square feet, then converts it to square meters.
'''

def main():
    CONVERSION_VALUE = 0.092903
    COST_PER_SQUARE_METER = 21.10
    length_feet = float(input("Enter the length of the office (in feet): "))
    width_feet = float(input("Enter the width of the office (in feet): "))
    office_area_feet = length_feet * width_feet
    office_area_square_meter = office_area_feet * CONVERSION_VALUE
    monthly_cost = office_area_square_meter * COST_PER_SQUARE_METER

    print(f"The area of the office is {office_area_feet:.2f} square feet")
    print(f"...which is {office_area_square_meter:.2f} square meters")
    print(f"......and you will pay €{monthly_cost:.2f} per month")

if __name__ == "__main__":
    main()
