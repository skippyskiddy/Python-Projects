'''
    Elif Tirkes
    CS 5001, Fall 2022
    Homework  1 - Program 1, Electric Bill

    This is a basic program to calculate one's electric bill for the month.
'''

def main():
    supply_charge = float(input("What is the supplier fee per kWh?: "))
    power_fee = float(input("What is the power fee per kWh?: "))
    kwh_hours = float(input("How many kWh were used this month?: "))
    total = (kwh_hours * supply_charge) + (kwh_hours * power_fee)
    print(f"Your electric bill this month is ${total:.2f}")


if __name__ == "__main__":
    main()
