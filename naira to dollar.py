# Currency Converter (Naira/Dollar)

# Estimated exchange rate 
NAIRA_PER_DOLLAR = 1500  # Example rate: 1 USD = 1500 NGN

def naira_to_dollar(amount):
    return amount / NAIRA_PER_DOLLAR

def dollar_to_naira(amount):
    return amount * NAIRA_PER_DOLLAR

def main():
    print("=== Currency Converter (Naira/ Dollar) ===")
    try:
        amount = float(input("Enter amount: "))
        print("Choose conversion:")
        print("1. Naira to Dollar")
        print("2. Dollar to Naira")
        
        choice = input("Enter 1 or 2: ").strip()
        
        if choice == "1":
            result = naira_to_dollar(amount)
            print(f"{amount} Naira = {result:.2f} Dollars")
        elif choice == "2":
            result = dollar_to_naira(amount)
            print(f"{amount} Dollars = {result:.2f} Naira")
        else:
            print(" Invalid choice. Please enter 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()