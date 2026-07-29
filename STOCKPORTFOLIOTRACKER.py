stocks = {
    "MTNN": 180,
    "GTCO": 250,
    "GOOG": 150,
    "DANSUGAR": 320
}

total = 0

with open("portfolio.txt", "w") as file:

    while True:
        stock = input("Enter stock name (or type QUIT to finish): ").upper()

        if stock == "QUIT":
            break

        if stock not in stocks:
            print("Stock not found!")
            continue

        quantity = int(input("Enter quantity: "))

        price = stocks[stock]
        value = price * quantity

        total += value

        print(f"{stock}: {quantity} × NGN{price} = NGN{value}")

        file.write(f"{stock}: {quantity} × NGN{price} = NGN{value}\n")

    print(f"\nTotal Investment Value = NGN{total}")
    file.write(f"\nTotal Investment Value = NGN{total}")