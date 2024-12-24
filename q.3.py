p_price = int(input("Product Price: "))
discount = int(input("Discount in percent: ").replace("%", ""))

cost = p_price - (p_price / 100) * discount

print("Price: ",cost)