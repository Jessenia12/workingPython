class Account:
    def __init__(self, balance=1000):
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +{amount}")
        else:
            print("Amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: -{amount}")

    def show_balance(self):
        print(f"Current balance: ${self.balance}")

    def show_transactions(self):
        for t in self.transactions:
            print(t)

def main():
    account = Account()
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check balance\n4. Show transactions\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            account.deposit(float(input("Enter amount: ")))
        elif choice == "2":
            account.withdraw(float(input("Enter amount: ")))
        elif choice == "3":
            account.show_balance()
        elif choice == "4":
            account.show_transactions()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
