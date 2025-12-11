# stock_portfolio.py
# A simple Stock Portfolio Tracker
# User enters stock symbols + quantity and program calculates total investment

from prices import STOCK_PRICES

def display_available_stocks():
    print("\nAvailable Stocks & Prices:")
    print("----------------------------")
    for stock, price in STOCK_PRICES.items():
        print(f"{stock} : ${price}")
    print("----------------------------\n")

def calculate_portfolio():
    print("📊 Welcome to the Stock Portfolio Tracker!")

    display_available_stocks()

    total_investment = 0
    portfolio = {}

    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print("❌ Stock not found! Please enter a valid symbol.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("❌ Invalid quantity! Enter a number.")
            continue

        # Store in portfolio dictionary
        portfolio[stock] = portfolio.get(stock, 0) + quantity

        print("✔ Added successfully!\n")

    print("\n==============================")
    print("📈 Your Stock Portfolio Summary")
    print("==============================")

    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        investment = price * qty
        total_investment += investment
        print(f"{stock} → Qty: {qty} × ${price} = ${investment}")

    print("------------------------------")
    print(f"💰 Total Investment: ${total_investment}")
    print("==============================")

    # Optional: save to file
    save = input("\nDo you want to save this result to a file? (yes/no): ").lower()

    if save == "yes":
        with open("portfolio_summary.txt", "w") as file:
            file.write("Stock Portfolio Summary\n")
            file.write("=======================\n")
            for stock, qty in portfolio.items():
                investment = STOCK_PRICES[stock] * qty
                file.write(f"{stock} → Qty: {qty} = ${investment}\n")
            file.write(f"\nTotal Investment: ${total_investment}\n")

        print("📄 Summary saved to portfolio_summary.txt")

if __name__ == "__main__":
    calculate_portfolio()
