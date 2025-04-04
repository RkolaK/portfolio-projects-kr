
# Fiber Optic Cable Cost Estimator

## Overview
This Python program calculates the total cost for purchasing fiber optic cable based on the length needed by a customer. It includes volume-based discounts and prints a receipt showing the total cost and savings, if applicable.

The program is interactive and prompts the user for input such as company name and length of cable required. Based on the quantity, it dynamically adjusts pricing using a tiered discount structure.

## Features
- Accepts user input for company name and cable length.
- Applies a tiered pricing model based on quantity:
  - >500 feet: $0.50/ft
  - 251–500 feet: $0.70/ft
  - 101–250 feet: $0.80/ft
  - ≤100 feet: $0.87/ft (standard price)
- Calculates and displays:
  - Total cost
  - Savings compared to standard price
  - A formatted receipt

## How to Use
1. Run the script in a Python environment (IDLE, terminal, or any IDE).
2. Enter the company name when prompted.
3. Enter the total feet of fiber optic cable needed.
4. View the final receipt with pricing and savings information.

## Technologies Used
- Python 3.x
- No external libraries required

## Example Output
```
Welcome, user!
Please, enter the company name: FiberCorp
Please, enter the total feet of fiber optic cable: 600

******************* Receipt *******************
Company name: FiberCorp
Quantity of fiber optic cable (ft): 600.0
Total cost: $ 300.00

You saved: $ 222.00
***********Thanks for shopping with us!***********
```

## Future Enhancements
- Add input validation for negative or zero values
- Save receipts to a text or CSV file
- Create a web or GUI interface
- Add sales tax and shipping options

## Author
KR  
Initial Release: March 27, 2023  
Latest Update: April 8, 2023
