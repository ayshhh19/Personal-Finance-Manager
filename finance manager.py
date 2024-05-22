class Transaction:
    """
    Represents a single financial transaction.
    """

    def _init_(self, date, description, amount):
        """
        Initializes a transaction with date, description, and amount.

        Args:
            date (str): Date of the transaction in YYYY-MM-DD format.
            description (str): Description of the transaction.
            amount (float): Amount of the transaction.
        """
        self.date = date
        self.description = description
        self.amount = amount


class FinanceManager:
    """
    Manages financial transactions and provides functionalities to add transactions, view transaction history, and calculate balance.
    """

    def _init_(self):
        """
        Initializes the FinanceManager with an empty list of transactions.
        """
        self.transactions = []

    def add_transaction(self, date, description, amount):
        """
        Adds a new transaction to the list.

        Args:
            date (str): Date of the transaction in YYYY-MM-DD format.
            description (str): Description of the transaction.
            amount (float): Amount of the transaction.
        """
        self.transactions.append(Transaction(date, description, amount))
        print("Transaction added successfully!")

    def view_transactions(self):
        """
        Displays the transaction history.
        """
        if self.transactions:
            print("\nTransaction History:")
            for index, transaction in enumerate(self.transactions, start=1):
                print(f"{index}. Date: {transaction.date}, Description: {transaction.description}, Amount: {transaction.amount}")
        else:
            print("Your transaction history is empty!")

    def calculate_balance(self):
        """
        Calculates the total income, total expenses, and current balance.
        """
        total_income = sum(transaction.amount for transaction in self.transactions if transaction.amount > 0)
        total_expenses = sum(transaction.amount for transaction in self.transactions if transaction.amount < 0)
        balance = total_income + total_expenses
        print(f"\nTotal Income: {total_income}")
        print(f"Total Expenses: {total_expenses}")
        print(f"Current Balance: {balance}")


def main():
    """
    Main function to run the Personal Finance Manager.
    """
    finance_manager = FinanceManager()

    while True:
        print("\n===== Personal Finance Manager =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Calculate Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = float(input("Enter income amount: "))
            finance_manager.add_transaction(date, description, amount)
        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = float(input("Enter expense amount: "))
            finance_manager.add_transaction(date, description, -amount)
        elif choice == "3":
            finance_manager.view_transactions()
        elif choice == "4":
            finance_manager.calculate_balance()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()