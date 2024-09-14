#!/usr/bin/env python3
# Jeff Bohn
# 9/13/2024
# Week 4 Lab 2 - How to Handle Exceptions

########## Exercise 8_1 ##########  

def get_number(prompt, low, high):
    while True:
        try:
            number = float(input(prompt))
            if number > low and number <= high:
                return number
            else:
                print(f"Entry must be greater than {low} " 
                    f"and less than or equal to {high}.")
        except ValueError as e:
            print("Enter Number only -------> ", e)
        except Exception as e:
            print("General Exception -------> ", e)

            
def get_integer(prompt, low, high):
    while True:
        try:
            number = int(input(prompt))
            if number > low and number <= high:
                return number
            else:
                print(f"Entry must be greater than {low} " 
                    f"and less than or equal to {high}.")
        except ValueError as e:
            print("Enter Integer only -------> ", e)
        except Exception as e:
            print("General Exception -------> ", e)


def calculate_future_value(monthly_investment, yearly_interest, years):

    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    future_value = 0.0
    for _ in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value


def main():
    choice = "y"
    while choice.lower() == "y":

        monthly_investment = get_number("Enter monthly investment:\t", 0, 1000)
        yearly_interest_rate = get_number("Enter yearly interest rate:\t", 0, 15)
        years = get_integer("Enter number of years:\t\t", 0, 50)

        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)
        
        print()
        print(f"Future value:\t\t\t{round(future_value, 2)}")
        print()

        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
