stock_prices = {
    "TCS": 180,
    "WIPRO": 250,
    "GOOG": 150,
    "MSFT": 300
}

stock = input("Enter Stock Name (TCS, WIPRO, GOOG, MSFT): ").upper()

if stock in stock_prices:
    quantity = int(input("Enter Quantity: "))
    total = stock_prices[stock] * quantity

    print("Stock:", stock)
    print("Price:", stock_prices[stock])
    print("Quantity:", quantity)
    print("Total Investment:", total)

else:
    print("Stock not found!")