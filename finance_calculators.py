# This task includes multiple codes to make a working financial calculators to provide a user with required information

import math

# We ask the user what calculation option they want to use.
calculation_type = input(""""
Investment- to calculate the amount of interest you'll earn on your investment.
Bond- to calculate the amount you'll have to pay on a home loan.

Please enter either 'investment' or 'bond' from the menu above to proceed: """).lower()

if calculation_type == "investment":
    # Asking the user for investment details
    P = float(input("Please enter the amount that you would like to deposit: "))
    rate = float(input("Please enter the rate of interest(Do not include %): "))
    t = float(input("Please enter the number of years for the investment: "))
    r = rate/100  # 'r' is the interest rate entered above divided by 100

    interest = input("Please enter the type of interest calculation for your investment(simple or compound): ")

# Now we simply calculate the total value of investment using provided information and the formula
    if interest == "simple":
        A = P*(1+r*t)
        print(f"Total value of your investment will be £{A} after {t} years at the rate of {rate}%.")
    elif interest == "compound":
        A = P*math.pow((1+r), t)
        print(f"Total value of your investment will be £{A} after {t} years at the rate of {rate}%.")
    else:
        print("Error! Please enter a valid interest type.")

    '''When calculation is based on the compound interest, total value of investment will significantly be higher 
    than the value of investment based on the simple interest. This is because the compound interest is calculated on 
    the principal amount plus the accumulated interest from previous periods. '''

elif calculation_type == "bond":
    # Asking the user for bond details
    P = float(input("Please enter the present value of the house: "))
    interest = float(input("Please enter the annual rate of interest(Do not include %): "))
    n = float(input("Please enter the number of months you plan to take to repay the bond: "))
    i = (interest/100)/12
    ''' i is the annual interest rate entered above divided by 100 and then by 12 to get the 
    monthly interest rate.'''

    # Now we calculate how much money the user will have to pay each month using the formula provided:
    repayment = (i*P)/(1-(1+i)**(-n))
    print(f"You will have to pay £{repayment} monthly for {n} months at the rate of {interest}%.")

else:
    print("Error! Please enter a valid option.")
