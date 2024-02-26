number_of_items = int(input("number of items: "))
total_price = []

for i in range(number_of_items):
    valid_input = False
    while not valid_input:
        price = float(input("Price of item: "))
        if price >= 0:
            total_price.append(price)
            valid_input = True
        else:
            print("Invalid input. Price must be 0 or greater.")

print("Total price: ", sum(total_price))
