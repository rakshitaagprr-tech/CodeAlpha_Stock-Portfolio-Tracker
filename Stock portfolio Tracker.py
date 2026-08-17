# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145
}

total_value = 0
portfolio = {}

print("===== Stock Portfolio Tracker =====")

while True:
    stock = input("Enter Stock Symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input(f"Enter quantity of {stock}: "))

    portfolio[stock] = quantity
    total_value += stock_prices[stock] * quantity

print("\n----- Portfolio Summary -----")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment Value = ${total_value}")

# Save to a text file
with open("portfolio_summary.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-------------------------\n")

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        file.write(f"{stock}: {quantity} shares = ${value}\n")

    file.write(f"\nTotal Investment Value = ${total_value}")

print("\nPortfolio saved successfully in 'portfolio_summary.txt'")
