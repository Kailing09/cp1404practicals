"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

# Constants
MAX_INCREASE = 0.175  # 17.5% maximum increase
MAX_DECREASE = 0.05   # 5% maximum decrease
MIN_PRICE = 1         # Minimum price of $1
MAX_PRICE = 100       # Maximum price of $100
INITIAL_PRICE = 50.0  # Starting price
OUTPUT_FILE = "stock_price_simulation.txt"  # Output file name

price = INITIAL_PRICE
days_past = 0

out_file = open(OUTPUT_FILE, 'w')

print(f"Starting price: ${price:,.2f}", file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    days_past += 1
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)

    print(f"On day {days_past} price is: ${price:,.2f}", file=out_file)

out_file.close()
