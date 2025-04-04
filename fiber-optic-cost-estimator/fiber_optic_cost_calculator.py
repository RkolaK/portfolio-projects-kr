# Author: KR
# Description: A program to calculate the total cost of fiber optic cable
# Date: 3/27/2023

# Change#:1
# Change(s) Made: Added error handling to check for invalid input - lines 29-36
#                 Added discount calculation and total savings - lines 42-52
#                 Added total savings print to the receipt - lines 59-60
# Date of Change: 3/31/2023

# Change#:2
# Change(s) Made: Created function to calculate total cost - lines 20-22
# Date of Change: 4/8/2023


# A Function to calculate the total cost
def calculate_total(feet, price):
    total = feet * price
    return total


def main():
    print('Welcome, user!')
    # Retrieve the company name and total feet of fiber optic cable
    company = input('Please, enter the company name: ')
    while True:
        try:
            total_feet = float(
                input('Please, enter the total feet of fiber optic '
                      'cable: '))
            break
        except ValueError:
            print('Please enter a number!')

    cost_per_ft = 0.87
    standard_cost = total_feet * cost_per_ft

    # Calculate the discount
    if total_feet > 500:
        cost_per_ft = 0.50
    elif total_feet > 250:
        cost_per_ft = 0.70
    elif total_feet > 100:
        cost_per_ft = 0.80

    # Calling the calculate_total function
    total_cost = calculate_total(total_feet, cost_per_ft)

    total_savings = standard_cost - total_cost

    # Print the receipt
    print('\n' + 'Receipt'.center(45, '*'))
    print('Company name:', company)
    print('Quantity of fiber optic cable (ft):', total_feet)
    print('Total cost: ${: .2f}'.format(total_cost))
    if total_savings != 0:
        print('\nYou saved: ${: .2f}'.format(total_savings))
    print('Thanks for shopping with us!'.center(45, '*'))


if __name__ == "__main__":
    main()
