import math

type_of_calculator = ["investment", "bond"]
interest = ["simple", "compound"]         

statement = """Choose either 'investment' or bond' from the menu below to proceed:

investment                     - to calculate the amount of interest you'll earn on interest
bond                           - to calculate the amount you'll have to pay on a home lone"""
print(statement)
print()

type_of_calculator = input("Please enter your decision. (investment or bond): ").lower()
if type_of_calculator != "investment" and type_of_calculator != "bond":
    print("Error message: enter either 'investment' or 'bond'")

if type_of_calculator == "investment":
    present_value = float(input("Please enter the amount of money that you are depositing: "))                 
    annual_rate = float(input("please enter the interest rate - (enter only the number and not the %): "))     
    interest_rate = annual_rate / 100
    num_of_years_investment = float(input("Please enter the number of years you plan to invest: "))            
    interest = input("Do you prefer 'simple'- or compounded interest? (simple or compound)").lower()

if interest == "simple":
    total_amount_simple = float(present_value) * (float(1) + float(interest_rate) * float(num_of_years_investment))
    print(round((total_amount_simple), 2))
    
if interest == "compound":
    total_amount_compound = float(present_value) * math.pow((float(1) + float(interest_rate)),float(num_of_years_investment))
    print(round((total_amount_compound), 2))
if type_of_calculator == "bond":

    present_value_of_house = float(input("Please enter the present value of the house: "))                          
    annual_rate_bond = float(input("Please input the interest rate - e.g. 7: "))               
    monthly_interest_rate = annual_rate_bond / float(12) / float(100)
    repayment_months = int(input("How many months do you plan on repayment of the loan - eg 120: "))   
    monthly_repayment = monthly_interest_rate * present_value_of_house / (1 - math.pow((1 + monthly_interest_rate), - repayment_months))
    print(round((monthly_repayment), 2))

# This is a python program to calculate investment and a home loan repayment(bond).
# The user input his choice of 'investment' or 'bond'
# If the user choose 'investment' then he can also choose simple can also choose the type of interest on the investment:
# Simple- or compounded interest
# 'Simple' interest refer to the interest on the initial investment
# 'Compound' refer to the interest that are accumulate after each period - the current value of the investment over time
# The math package is imported to account for the formulas used in two of the 3 calculations: math.pow
# "Math.pow" means the exponent of a number or/and numbers.









                                      
                                           
