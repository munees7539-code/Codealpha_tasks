# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

total_investment = 0
portfolio = {}

print("Available Stocks:", list(stock_prices.keys()))

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    
    if stock in stock_prices:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = quantity
        investment = stock_prices[stock] * quantity
        total_investment += investment
    else:
        print(" Stock not available!")

print("\n Portfolio Summary")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares × {stock_prices[stock]} = {qty * stock_prices[stock]}")

print("\n Total Investment Value:", total_investment)

# Optional: Save to file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    for stock, qty in portfolio.items():
        file.write(f"{stock}: {qty} shares\n")
    file.write(f"\nTotal Investment Value: {total_investment}")

print("\n Portfolio saved to portfolio.txt")
