"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))

while sales >= 0:
    bonus = 0.10
    bonus_extra = 0.15

    if sales >= 1000:
        bonus_amount = sales * bonus_extra
    else:
        bonus_amount = sales * bonus

    print(bonus_amount)
    sales = float(input("Enter sales: $"))

print("code ended")
