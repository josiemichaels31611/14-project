prices = [25.0, 50.0, 75.0, 100.0, 150.0,]
print(prices)
def apply_discount(price):
    return .8 * price
new_prices = map(apply_discount, prices)
print(list(new_prices))