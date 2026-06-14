import time

print("=" * 70)
print("          ADVANCED STOCK PORTFOLIO TRACKER")
print("=" * 70)

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 135,
    "META": 300,
    "NVDA": 500,
    "IBM": 145,
    "ORCL": 120,
    "NFLX": 450
}

portfolio = {}

while True:

    print("\n" + "=" * 70)
    print("1. View Available Stocks")
    print("2. Add Stock")
    print("3. View Portfolio")
    print("4. Search Stock")
    print("5. Calculate Total Investment")
    print("6. Save Report")
    print("7. Exit")
    print("=" * 70)

    choice = input("Enter Choice : ")

    if choice == "1":

        print("\nAVAILABLE STOCKS")
        print("-" * 50)

        for stock, price in stocks.items():
            print(stock, ":", price)

    elif choice == "2":

        stock_name = input("Enter Stock Name : ").upper()

        if stock_name in stocks:

            quantity = int(input("Enter Quantity : "))

            price = stocks[stock_name]
            investment = quantity * price

            portfolio[stock_name] = {
                "Price": price,
                "Quantity": quantity,
                "Investment": investment
            }

            print("Stock Added Successfully!")

        else:
            print("Stock Not Found!")

    elif choice == "3":

        print("\nPORTFOLIO DETAILS")
        print("-" * 50)

        if len(portfolio) == 0:
            print("Portfolio Empty")

        else:

            for stock, details in portfolio.items():

                print("\nStock :", stock)
                print("Price :", details["Price"])
                print("Quantity :", details["Quantity"])
                print("Investment :", details["Investment"])

    elif choice == "4":

        search = input("Enter Stock Name : ").upper()

        if search in portfolio:

            print("\nStock Found")
            print("Price :", portfolio[search]["Price"])
            print("Quantity :", portfolio[search]["Quantity"])
            print("Investment :", portfolio[search]["Investment"])

        else:
            print("Stock Not Available")

    elif choice == "5":

        total = 0

        for details in portfolio.values():
            total += details["Investment"]

        print("\nTotal Portfolio Value :", total)

    elif choice == "6":

        file = open("portfolio_report.txt", "w")

        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("=" * 50 + "\n")

        total = 0

        for stock, details in portfolio.items():

            file.write("\nStock : " + stock + "\n")
            file.write("Price : " + str(details["Price"]) + "\n")
            file.write("Quantity : " + str(details["Quantity"]) + "\n")
            file.write("Investment : " + str(details["Investment"]) + "\n")

            total += details["Investment"]

        file.write("\nTotal Portfolio Value : " + str(total))

        file.close()

        print("Report Saved Successfully!")

    elif choice == "7":

        print("\nGenerating Report...")
        time.sleep(2)

        total = 0

        for details in portfolio.values():
            total += details["Investment"]

        print("Final Portfolio Value :", total)
        print("Thank You For Using Stock Portfolio Tracker")
        break

    else:
        print("Invalid Choice")