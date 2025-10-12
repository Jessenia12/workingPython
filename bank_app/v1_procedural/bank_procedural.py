balance = 1000
transactions = []

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        transactions.append(f"Deposit: +{amount}")
    else:
        print("Amount must be positive.")

def withdraw(amount):
    global balance
    if 0 < amount <= balance:
        balance -= amount
        transactions.append(f"Withdraw: -{amount}")
    else:
        print("Insufficient funds or invalid amount.")

def show_balance():
    print(f"Current balance: ${balance}")

def show_transactions():
    for t in transactions:
        print(t)

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check balance\n4. Show transactions\n5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        deposit(float(input("Enter amount: ")))
    elif choice == "2":
        withdraw(float(input("Enter amount: ")))
    elif choice == "3":
        show_balance()
    elif choice == "4":
        show_transactions()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
